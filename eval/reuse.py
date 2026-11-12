"""Reuse the finished runs of another results folder, so an eval does not pay for them again.

An arm of this eval takes the runs of the arm in the other folder whose plugin has the
same files. The arm with no plugin takes the other folder's runs with no plugin. A run is
taken only when it ran on the same model and has a turn for every turn of the task. Where
its done.json records them, the effort and the task must match too; runs from before
2026-11-12 record neither.

The copy writes the new run folder's path into the transcripts. An agent's transcript
holds the path of its work folder, which names the arm and the run, and the blind
samples hide only the run's own path.
"""
import json
import shutil
import subprocess

from run import REPO, task_stamp


def ref_files(ref):
    """{path under plugin/: blob hash} for the plugin at a git ref."""
    out = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", ref, "plugin"],
                         capture_output=True, text=True, check=True).stdout
    return {path.removeprefix("plugin/"): meta.split()[2]
            for meta, path in (line.split("\t", 1) for line in out.splitlines())}


def folder_files(folder):
    """{path: blob hash} for a plugin folder on disk."""
    files = sorted(p for p in folder.rglob("*") if p.is_file())
    if not files:
        return {}
    shas = subprocess.run(["git", "hash-object", "--", *map(str, files)],
                          capture_output=True, text=True, check=True).stdout.split()
    return {str(p.relative_to(folder)): sha for p, sha in zip(files, shas)}


def match_arms(source, refs, none):
    """{arm of this eval: the arm of the source folder whose runs it may take}."""
    found = {d.name: folder_files(d / "plugin") for d in sorted((source / "raw" / "arms").glob("*"))}
    arms = {}
    for arm, ref in refs.items():
        same = [name for name, files in found.items() if files and files == ref_files(ref)]
        if same:
            arms[arm] = arm if arm in same else same[0]
    if none:
        arms["none"] = "none"
    return arms


def session_model(run_dir):
    """The model in the start event of the run's first turn, or None."""
    first = run_dir / "turn-1.jsonl"
    for line in first.read_text().splitlines() if first.exists() else []:
        if line.startswith("{"):
            event = json.loads(line)
            if event.get("type") == "system" and event.get("subtype") == "init":
                return event.get("model")
    return None


def usable(run_dir, task, model, effort):
    """True when the run is finished and ran what this eval would run."""
    done = run_dir / "done.json"
    if not done.exists() or len(list(run_dir.glob("turn-*.jsonl"))) != len(task["turns"]):
        return False
    info = json.loads(done.read_text())
    return (info.get("model") or session_model(run_dir)) == model \
        and info.get("effort", effort) == effort and info.get("task", task_stamp(task)) == task_stamp(task)


def plan(source, refs, none, tasks, runs, raw, model, effort, taken=()):
    """Return [(source run folder, new run folder)]. Only places with no finished run, and not in taken, get a run."""
    pairs, taken = [], set(taken)
    for arm, from_arm in match_arms(source, refs, none).items():
        for t in tasks:
            mine = raw / t["name"]
            free = [mine / f"{arm}-{i}" for i in range(1, runs + 1)
                    if not (mine / f"{arm}-{i}" / "done.json").exists() and mine / f"{arm}-{i}" not in taken]
            found = sorted((d for d in (source / "raw" / t["name"]).glob(f"{from_arm}-*")
                            if d.name.rsplit("-", 1)[1].isdigit() and usable(d, t, model, effort)),
                           key=lambda d: int(d.name.rsplit("-", 1)[1]))
            pairs += list(zip(found, free))
            taken.update(dst for _, dst in zip(found, free))
    return pairs


def copy(pairs):
    """Copy each run, and write its new path into its transcripts."""
    for src, dst in pairs:
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(src, dst, symlinks=True)
        for turn in dst.glob("turn-*.jsonl"):
            turn.write_text(turn.read_text().replace(str(src), str(dst)))
