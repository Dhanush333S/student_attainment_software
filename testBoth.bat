@echo off
rem First terminal
start cmd /k "cd /d E:\Student Attainment Project\Student Attainment Analyzer\Student-Performance-Analyzer\Student-Performance-Analyzer && call school\Scripts\activate && python run.py"

rem Second terminal
start cmd /k "cd /d E:\Student Attainment Project\Student Attainment Analyzer\Student-Performance-Analyzer\Student-Performance-Analyzer && call school\Scripts\activate && cd /d E:\Student Attainment Project\Student Attainment Analyzer\Network && python hosted_run.py"

exit
