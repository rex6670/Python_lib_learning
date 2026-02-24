from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(rel_path: str, name: str):
    path = REPO_ROOT / rel_path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_day01_scan_project_filters_suffixes(tmp_path: Path):
    m = load_module("Day01/day01_inventory.py", "day01_inventory")

    (tmp_path / "a.def").write_text("x", encoding="utf-8")
    (tmp_path / "b.lef").write_text("x", encoding="utf-8")
    (tmp_path / "c.txt").write_text("x", encoding="utf-8")

    rows = m.scan_project(tmp_path)
    paths = {r["path"] for r in rows}
    assert paths == {"a.def", "b.lef"}


def test_day02_parse_name_and_hash(tmp_path: Path):
    m = load_module("Day02/day02_parse_and_hash.py", "day02_parse")

    parsed = m.parse_name("topcpu_v12_FF_0p72V_125C.def")
    assert parsed is not None
    assert parsed["design"] == "topcpu"
    assert parsed["corner"] == "FF"
    assert m.parse_name("top_cpu_v12_FF_0p72V_125C.def") is None
    assert m.parse_name("bad_name.def") is None

    p = tmp_path / "sample.txt"
    p.write_text("abc", encoding="utf-8")
    assert m.sha256_file(p) == hashlib.sha256(b"abc").hexdigest()


def test_day03_run_job_success_and_timeout():
    m = load_module("Day03/day03_tool_runner.py", "day03_runner")

    code, out, err = m.run_job(["python", "-c", "print('ok')"], timeout_s=5)
    assert code == 0
    assert out.strip() == "ok"
    assert err == ""

    code2, _, err2 = m.run_job(["python", "-c", "import time; time.sleep(2)"], timeout_s=1)
    assert code2 == 1
    assert err2 == "exception"


def test_day04_load_config(tmp_path: Path):
    m = load_module("Day04/day04_cli_flow.py", "day04_cli")

    cfg_path = tmp_path / "flow.ini"
    cfg_path.write_text("[N7]\nthreads=8\n", encoding="utf-8")
    cfg = m.load_config(cfg_path)
    assert "N7" in cfg.sections()
    assert cfg["N7"]["threads"] == "8"


def test_day05_build_demo_frames_shape():
    pd = pytest.importorskip("pandas")
    m = load_module("Day05/day05_qor_analysis.py", "day05_qor")

    baseline, exp = m.build_demo_frames()
    assert isinstance(baseline, pd.DataFrame)
    assert isinstance(exp, pd.DataFrame)
    assert list(baseline.columns) == ["block", "corner", "wns", "tns"]


def test_day06_generate_and_bbox_numpy():
    pytest.importorskip("pandas")
    pytest.importorskip("scipy")
    m = load_module("Day06/day06_million_objects_storage.py", "day06_storage")

    x, y, layer, orient = m.generate_data(n=1000, seed=1)
    assert len(x) == len(y) == len(layer) == len(orient) == 1000
    cnt = m.bbox_numpy(x, y, 0, 99_999, 0, 99_999)
    assert cnt == 1000


def test_day07_density_bin_sum_matches_points():
    pytest.importorskip("numba")
    np = pytest.importorskip("numpy")
    m = load_module("Day07/day07_numba_opt.py", "day07_numba")

    x = np.array([0, 10, 20, 30], dtype=np.int32)
    y = np.array([0, 10, 20, 30], dtype=np.int32)
    out = m.density_bin(x, y, grid=10, max_xy=100)
    assert int(out.sum()) == 4


def test_day08_tasks(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    m = load_module("Day08/day08_parallel_jobs.py", "day08_parallel")

    monkeypatch.chdir(tmp_path)
    Path("Day08").mkdir()
    name = m.io_task(3)
    assert name == "tmp_3.txt"
    assert (tmp_path / "Day08" / "tmp_3.txt").read_text(encoding="utf-8") == "job=3\n"
    assert isinstance(m.cpu_task(2), int)


def test_day09_risky_step():
    m = load_module("Day09/day09_observability.py", "day09_obs")

    assert m.risky_step(5) == 2
    with pytest.raises(ZeroDivisionError):
        m.risky_step(0)


def test_day10_check_job_is_deterministic():
    pytest.importorskip("pandas")
    pytest.importorskip("numpy")
    m = load_module("Day10/day10_capstone.py", "day10_capstone")

    j1 = m.check_job(7)
    j2 = m.check_job(7)
    assert j1 == j2
    assert set(j1.keys()) == {"job_id", "wns", "status"}
