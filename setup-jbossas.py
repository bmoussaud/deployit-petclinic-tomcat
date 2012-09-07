def newEnv(envName,serverName,shifts,common):
	members=[]
	repository.delete('Environments/'+envName)
	repository.delete('Infrastructure/host-%s-vm' % (serverName))
	repository.delete('Environments/Dict-%s' % (serverName))
	host=repository.create(factory.configurationItem('Infrastructure/host-%s-vm' % (serverName), 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
	members.append(host.id)
	data=repository.create(factory.configurationItem('Environments/Dict-'+serverName, 'udm.Dictionary', {'entries':{'jbossas.TransactionalDatasource.userName':'User'+serverName,'jbossas.TransactionalDatasource.password':'tiger'}}))
	#members.append(data.id)
	sql=repository.create(factory.configurationItem(host.id+'/sql-'+serverName, 'sql.MySqlClient', {'host':host.id,'mySqlHome':'/usr','databaseName':'petclinicDev','username':'root','password':'xebialabs','deploymentGroup':'1'}))
	members.append(sql.id)
	for (i,shift) in enumerate(shifts):
		idx=i+1
		groupName=str(idx+2)
		server=repository.create(factory.configurationItem(host.id+'/'+serverName+'-'+str(idx), 'jbossas.ServerV4', {'host':host.id,'home':'/home/ubuntu/jboss/jboss-4.2.3.GA','serverName':serverName+'-'+str(idx),'httpPort': ''+str(8080+shift),'ajpPort':''+str(8009+shift),'controlPort':''+str(1099+shift),'deploymentGroup':groupName}))
		members.append(server.id)
		testRunner=repository.create(factory.configurationItem(host.id+'/testRunner-'+serverName+'-'+str(idx), 'tests2.TestRunner', {'host':host.id,'deploymentGroup':groupName, 'envVars':{'PORT':''+str(8080+shift)}}))
		members.append(testRunner.id)

	env = repository.create(factory.configurationItem('Environments/'+envName, 'udm.Environment', {'members':members, 'dictionaries':[data.id, common.id]}))
	return env



common=repository.read('Environments/DictCommon')
values = common.values['entries']
values['jbossas.TransactionalDatasource.driverClass']='com.mysql.jdbc.Driver'
values['jbossas.TransactionalDatasource.connectionUrl']='jdbc:mysql://localhost/petclinic'
values['tests2.ExecutedHttpRequestTest.url']='http://deployit.vm:$PORT/petclinic/index.jsp' 
common.values['entries']=values
repository.update(common)

newEnv('jboss-DEV','jboss-dev',[100],common)
newEnv('jboss-TEST','jboss-test',[200,300],common)
newEnv('jboss-PROD','jboss-prod',[400,500,600,700],common)



