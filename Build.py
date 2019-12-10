import MsBuilder, SolutionFinder
rootFolder="ProjectFolder"
if result == False:
    print('build failed')

solutionFinder = SolutionFinder.SolutionFinder(rootFolder)
msBuilder = MsBuilder.MsBuilder()  # create our instance
for solutionPath in solutionFinder.Solutions:
    result = msBuilder.run(solutionPath)
    if result == False:
        print('build failed')

