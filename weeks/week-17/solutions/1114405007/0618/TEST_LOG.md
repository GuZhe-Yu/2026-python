# TEST_LOG — 6/18 搜尋效能五階段專題

執行指令：`python -m unittest discover . "test_*.py" -v`

```
$ python -m unittest discover . "test_*.py" -v

test_benchmark_overwrites_old_json ... ok
test_benchmark_runs_and_creates_json ... ok
test_results_json_has_correct_structure ... ok
test_results_values_are_positive ... ok
test_plot_creates_png ... ok
test_plot_overwrites_old_png ... ok
test_png_is_nonempty ... ok
test_duplicate_values ... ok
test_empty_list ... ok
test_first_and_last_position ... ok
test_found_target_returns_positive ... ok
test_input_not_mutated ... ok
test_not_found_returns_negative ... ok
test_single_element_found ... ok
test_single_element_not_found ... ok
test_binary_search_explicitly_checks_none_data ... ok
test_binary_search_explicitly_checks_none_target ... ok
test_plot_guarantees_figure_close_on_error ... ok
test_timing_no_broad_except ... ok
test_default_repeat_is_three ... ok
test_exception_in_wrapped_not_recorded ... ok
test_preserves_function_metadata ... ok
test_repeat_below_one_raises_valueerror ... ok
test_repeat_non_integer_raises_typeerror ... ok
test_repeat_records_and_average ... ok
test_returns_original_result ... ok
----------------------------------------------------------------------
Ran 26 tests in 0.914s
OK
```

## 各階段測試統計

| Stage | 測試檔 | 數量 | 結果 |
|-------|--------|------|------|
| 1 | `test_timing.py` | 7 | ok |
| 2 | `test_search.py` | 8 | ok |
| 3 | `test_benchmark.py` | 4 | ok |
| 4 | `test_plot.py` | 3 | ok |
| 5 | `test_security.py` | 4 | ok |
| **合計** | | **26** | **OK** |
