import MsBuilder
import SolutionFinder
rootFolder="ProjectFolder"
excludedProjects = ["ExcludeSomePath"]
solutionFinder = SolutionFinder.SolutionFinder(rootFolder)
msBuilder = MsBuilder.MsBuilder()  # create our instance
for solutionPath in solutionFinder.Solutions:
    if solutionPath not in excludedProjects:
        print(solutionPath)
        result = msBuilder.run(solutionPath)
        if result == False:
            print('build failed')
