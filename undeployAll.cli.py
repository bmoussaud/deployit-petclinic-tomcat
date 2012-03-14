for a in repository.search("udm.DeployedApplication"):
	print "Undeploy",a
	deployit.startTaskAndWait(deployment.undeploy(a).taskId)


map(repository.delete, repository.search('udm.Environment'))
map(repository.delete, repository.search('udm.Dictionary'))
map(repository.delete, repository.search('core.Directory'))
map(repository.delete, repository.search('overthere.SshHost'))

