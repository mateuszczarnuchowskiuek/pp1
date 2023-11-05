#9. A test is passed when the number of correctly completed tasks is at least 50%. Write a program that checks whether the test is passed. The total number of test tasks and the number of correctly completed tasks are included in variables. Sample result:
#Test passed

totalNumberOfTestTasks = 50
totalNumberOfCorrectlyCompletedTasks = 25

if totalNumberOfCorrectlyCompletedTasks >= (totalNumberOfTestTasks/2):
    print('test passed')