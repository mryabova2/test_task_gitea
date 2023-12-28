<h2>Test Task</h2>
<h4><img src="icons/tools.png" height="15" align="center"/> Here are steps to run it</h4>
<p><i>You will need python and poetry installed</i><br>

<p><img src="icons/check.png" height="10"/> Open bash <br>
<img src="icons/check.png" height="10"/> <b>Run:</b> <i>git clone https://github.com/mryabova2/test_task_gitea.git</i><br>
<img src="icons/check.png" height="10"/> <b>In downloaded project go to gitea_tests folder:</b>
<i>cd /test_task_gitea/gitea_tests/</i><br>
<img src="icons/check.png" height="10"/> <b>Install requirements by:</b>
<i>poetry install</i><br>
<img src="icons/check.png" height="10"/> <b>Activate environment:</b>
<i>poetry shell</i><br>
<img src="icons/check.png" height="10"/> <b>Run test:</b>
<i>pytest tests.py</i><br>
<img src="icons/check.png" height="10"/> <b>Check allure report after tests:</b>
<i>allure serve allure_results</i><br>
