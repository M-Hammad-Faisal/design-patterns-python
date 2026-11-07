"""Run every pattern script and report which ones succeed."""
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
scripts = sorted(root.glob("*Pattern/*Pattern.py"))
failed = []
for script in scripts:
    result = subprocess.run([sys.executable, script.name], cwd=script.parent,
                            capture_output=True, text=True, timeout=60)
    status = "ok" if result.returncode == 0 else "FAILED"
    print(f"{status:7} {script.relative_to(root)}")
    if result.returncode != 0:
        failed.append(script)
        print(result.stderr[-500:])
print(f"\n{len(scripts) - len(failed)}/{len(scripts)} scripts ran successfully")
sys.exit(1 if failed else 0)
