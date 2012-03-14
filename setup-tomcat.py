#Application
#app=repository.create(factory.configurationItem('Applications/PetPortal','udm.Application',{'deploymentPipeline':['Environments/Tomcat-Dev','Environments/Tomcat-Test','Environments/Tomcat-Acc','Environments/Tomcat-Production']}))

common=repository.create(factory.configurationItem('Environments/DictCommon', 'udm.Dictionary', {'entries':{'tomcat.DataSource.driverClassName':'com.mysql.jdbc.Driver','tomcat.DataSource.url':'jdbc:mysql://localhost/petclinic','tomcat.DataSource.context':'petclinic','TITLE':'Demo by Benoit','tests2.ExecutedHttpRequestTest.expectedResponseText':'Home','tests2.HttpRequestTester.showPageInConsole':'true'}}))

repository.create(factory.configurationItem('Environments/DevelopmentDirectory','core.Directory'))
repository.create(factory.configurationItem('Environments/TestDirectory','core.Directory'))
repository.create(factory.configurationItem('Environments/AcceptanceDirectory','core.Directory'))
repository.create(factory.configurationItem('Environments/ProductionDirectory','core.Directory'))

#DEV
host=repository.create(factory.configurationItem('Infrastructure/host-ubuntu-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcatdev=repository.create(factory.configurationItem(host.id+'/tomcat-dev', 'tomcat.Server', {'host':host.id,'home':'/home/ubuntu/tomcat/tomcat-dev','startCommand':'nohup /home/ubuntu/tomcat/tomcat-dev/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-dev/bin/shutdown.sh'}))
testRunner=repository.create(factory.configurationItem(host.id+'/testRunner', 'tests2.TestRunner', {'host':host.id}))
vh=repository.create(factory.configurationItem(tomcatdev.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcatdev.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatDev', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserDev','tomcat.DataSource.password':'tiger','tests2.ExecutedHttpRequestTest.url':'http://deployit.vm:8080/petclinic/index.jsp'}}))
sql=repository.create(factory.configurationItem(host.id+'/sql-dev', 'sql.MySqlClient', {'host':host.id,'mySqlHome':'/usr','databaseName':'deployit','username':'root','password':'xebialabs'}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Dev', 'udm.Environment', {'members':[host.id, tomcatdev.id, vh.id, testRunner.id,sql.id], 'dictionaries':[data.id, common.id]}))

#TEST
host=repository.create(factory.configurationItem('Infrastructure/host-test-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcatdev=repository.create(factory.configurationItem(host.id+'/tomcat-test', 'tomcat.Server', {'host':host.id,'home':'/home/ubuntu/tomcat/tomcat-test','startCommand':'nohup /home/ubuntu/tomcat/tomcat-test/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-test/bin/shutdown.sh'}))
vh=repository.create(factory.configurationItem(tomcatdev.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcatdev.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatTest', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserTest','tomcat.DataSource.password':'lion','tests2.ExecutedHttpRequestTest.url':'http://deployit.vm:9080/petclinic/index.jsp'}}))
testRunner=repository.create(factory.configurationItem(host.id+'/testRunner', 'tests2.TestRunner', {'host':host.id}))
sql=repository.create(factory.configurationItem(host.id+'/sql-test', 'sql.MySqlClient', {'host':host.id,'mySqlHome':'/usr','databaseName':'deployit','username':'root','password':'xebialabs'}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Test', 'udm.Environment', {'members':[host.id, tomcatdev.id, vh.id, testRunner.id,sql.id], 'dictionaries':[data.id, common.id],'released':'true'}))

#ACC
host=repository.create(factory.configurationItem('Infrastructure/host-acc-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcatdev=repository.create(factory.configurationItem(host.id+'/tomcat-acc', 'tomcat.Server', {'host':host.id,'home':'/home/ubuntu/tomcat/tomcat-acc','startCommand':'nohup /home/ubuntu/tomcat/tomcat-acc/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-acc/bin/shutdown.sh'}))
vh=repository.create(factory.configurationItem(tomcatdev.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcatdev.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatAcc', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserAcc','tomcat.DataSource.password':'zebra','tests2.ExecutedHttpRequestTest.url':'http://deployit.vm:10080/petclinic/index.jsp'}}))
testRunner=repository.create(factory.configurationItem(host.id+'/testRunner', 'tests2.TestRunner', {'host':host.id}))
sql=repository.create(factory.configurationItem(host.id+'/sql-acc', 'sql.MySqlClient', {'host':host.id,'mySqlHome':'/usr','databaseName':'deployit','username':'root','password':'xebialabs'}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Acc', 'udm.Environment', {'members':[host.id, tomcatdev.id, vh.id, testRunner.id,sql.id], 'dictionaries':[data.id, common.id],'isUserTested':'true'}))


#PROD
host1=repository.create(factory.configurationItem('Infrastructure/host-prod-1-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
host2=repository.create(factory.configurationItem('Infrastructure/host-prod-2-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcat1=repository.create(factory.configurationItem(host1.id+'/tomcat-prod-1', 'tomcat.Server', {'host':host1.id,'home':'/home/ubuntu/tomcat/tomcat-prod-1','startCommand':'nohup /home/ubuntu/tomcat/tomcat-prod-1/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-prod-1/bin/shutdown.sh'}))
tomcat2=repository.create(factory.configurationItem(host2.id+'/tomcat-prod-2', 'tomcat.Server', {'host':host2.id,'home':'/home/ubuntu/tomcat/tomcat-prod-2','startCommand':'nohup /home/ubuntu/tomcat/tomcat-prod-2/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-prod-2/bin/shutdown.sh'}))
vh1=repository.create(factory.configurationItem(tomcat1.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcat1.id}))
vh2=repository.create(factory.configurationItem(tomcat2.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcat2.id}))
testRunner1=repository.create(factory.configurationItem(host1.id+'/testRunner', 'tests2.TestRunner', {'host':host1.id}))
testRunner2=repository.create(factory.configurationItem(host2.id+'/testRunner', 'tests2.TestRunner', {'host':host2.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatProduction', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserProduction','tomcat.DataSource.password':'cat','tests2.ExecutedHttpRequestTest.url':'http://deployit.vm:11080/petclinic/index.jsp'}}))
sql=repository.create(factory.configurationItem(host1.id+'/sql-prod', 'sql.MySqlClient', {'host':host1.id,'mySqlHome':'/usr','databaseName':'deployit','username':'root','password':'xebialabs'}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Production', 'udm.Environment', {'members':[host1.id, tomcat1.id, vh1.id,host2.id, tomcat2.id, vh2.id, testRunner1.id, testRunner2.id,sql.id ], 'dictionaries':[data.id, common.id],'isPerformanceTested':'true','isUserTested':'true'}))


#Moving
repository.move('Environments/Tomcat-Dev','Environments/DevelopmentDirectory/Tomcat-Dev')
repository.move('Environments/Tomcat-Test','Environments/TestDirectory/Tomcat-Test')
repository.move('Environments/Tomcat-Acc','Environments/AcceptanceDirectory/Tomcat-Acc')
repository.move('Environments/Tomcat-Production','Environments/ProductionDirectory/Tomcat-Production')

repository.move('Environments/DictTomcatDev','Environments/DevelopmentDirectory/Dict-Dev')
repository.move('Environments/DictTomcatTest','Environments/TestDirectory/Dict-Test')
repository.move('Environments/DictTomcatAcc','Environments/AcceptanceDirectory/Dict-Acc')
repository.move('Environments/DictTomcatProduction','Environments/ProductionDirectory/Dict-Production')
#Users
security.createUser('dev','dev')
security.createUser('test','test')
security.createUser('acc','acc')
security.createUser('prod','prod')

security.assignRole("developers", ["dev"])
security.assignRole("testers", ["test"])
security.assignRole("accepters", ["acc"])
security.assignRole("ops", ["prod"])

security.grant("login", "developers" )
security.grant("login", "testers" )
security.grant("login", "accepters" )
security.grant("login", "ops" )

security.grant("read", "developers", ['Applications'] )
security.grant("read", "testers",['Applications'] )
security.grant("read", "accepters",['Applications'] )
security.grant("read", "ops" , ['Applications'])

security.grant("repo#edit", "developers", ['Applications'] )
security.grant("repo#edit", "testers",['Applications'] )
security.grant("repo#edit", "accepters",['Applications'] )
security.grant("repo#edit", "ops" , ['Applications'])




security.grant("import#initial", "developers" )
security.grant("import#upgrade", "developers" )
security.grant("deploy#initial", "developers", ['Environments/DevelopmentDirectory'])
security.grant("deploy#upgrade", "developers", ['Environments/DevelopmentDirectory'])
security.grant("task#skip_step", "developers", ['Environments/DevelopmentDirectory'])

security.grant("deploy#initial", "testers", ['Environments/TestDirectory'])
security.grant("deploy#upgrade", "testers", ['Environments/TestDirectory'])
security.grant("task#skip_step", "testers", ['Environments/TestDirectory'])

security.grant("deploy#initial", "accepters", ['Environments/AcceptanceDirectory'])
security.grant("deploy#upgrade", "accepters", ['Environments/AcceptanceDirectory'])
security.grant("task#skip_step", "accepters", ['Environments/AcceptanceDirectory'])

security.grant("deploy#initial", "ops", ['Environments/ProductionDirectory'])
security.grant("deploy#upgrade", "ops", ['Environments/ProductionDirectory'])
security.grant("task#skip_step", "ops", ['Environments/ProductionDirectory'])

security.grant('read','developers',['Environments/DevelopmentDirectory','Environments/TestDirectory','Environments/AcceptanceDirectory','Environments/ProductionDirectory'])
security.grant('read','testers',['Environments/DevelopmentDirectory','Environments/TestDirectory','Environments/AcceptanceDirectory','Environments/ProductionDirectory'])
security.grant('read','accepters',['Environments/DevelopmentDirectory','Environments/TestDirectory','Environments/AcceptanceDirectory','Environments/ProductionDirectory'])
security.grant('read','ops',['Environments/DevelopmentDirectory','Environments/TestDirectory','Environments/AcceptanceDirectory','Environments/ProductionDirectory'])



