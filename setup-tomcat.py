
common=repository.create(factory.configurationItem('Environments/DictCommon', 'udm.Dictionary', {'entries':{'tomcat.DataSource.driverClassName':'com.mysql.jdbc.Driver','tomcat.DataSource.url':'jdbc:mysql://localhost/petclinic','tomcat.DataSource.context':'petclinic','TITLE':'Demo by Benoit'}}))

host=repository.create(factory.configurationItem('Infrastructure/host-ubuntu-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcatdev=repository.create(factory.configurationItem(host.id+'/tomcat-dev', 'tomcat.Server', {'host':host.id,'home':'/home/ubuntu/tomcat/tomcat-dev','startCommand':'nohup /home/ubuntu/tomcat/tomcat-dev/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-dev/bin/shutdown.sh'}))
vh=repository.create(factory.configurationItem(tomcatdev.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcatdev.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatDev', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserDev','tomcat.DataSource.password':'tiger'}}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Dev', 'udm.Environment', {'members':[host.id, tomcatdev.id, vh.id], 'dictionaries':[data.id, common.id]}))
deployit.print(env)

host=repository.create(factory.configurationItem('Infrastructure/host-integration-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcatdev=repository.create(factory.configurationItem(host.id+'/tomcat-integration', 'tomcat.Server', {'host':host.id,'home':'/home/ubuntu/tomcat/tomcat-integration','startCommand':'nohup /home/ubuntu/tomcat/tomcat-integration/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-integration/bin/shutdown.sh'}))
vh=repository.create(factory.configurationItem(tomcatdev.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcatdev.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatIntegration', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserIntegration','tomcat.DataSource.password':'lion'}}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Integration', 'udm.Environment', {'members':[host.id, tomcatdev.id, vh.id], 'dictionaries':[data.id, common.id]}))
deployit.print(env)

host1=repository.create(factory.configurationItem('Infrastructure/host-prod-1-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
host2=repository.create(factory.configurationItem('Infrastructure/host-prod-2-vm', 'overthere.SshHost', {'address':'deployit.vm','os':'UNIX', 'connectionType':'SFTP', 'username':'ubuntu', 'password':'ubuntu'}))
tomcat1=repository.create(factory.configurationItem(host1.id+'/tomcat-prod-1', 'tomcat.Server', {'host':host1.id,'home':'/home/ubuntu/tomcat/tomcat-prod-1','startCommand':'nohup /home/ubuntu/tomcat/tomcat-prod-1/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-prod-1/bin/shutdown.sh'}))
tomcat2=repository.create(factory.configurationItem(host2.id+'/tomcat-prod-2', 'tomcat.Server', {'host':host2.id,'home':'/home/ubuntu/tomcat/tomcat-prod-2','startCommand':'nohup /home/ubuntu/tomcat/tomcat-prod-2/bin/startup.sh && sleep 5','stopCommand':'/home/ubuntu/tomcat/tomcat-prod-2/bin/shutdown.sh'}))
vh1=repository.create(factory.configurationItem(tomcat1.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcat1.id}))
vh2=repository.create(factory.configurationItem(tomcat2.id+'/defaultVH', 'tomcat.VirtualHost', {'server':tomcat2.id}))
data=repository.create(factory.configurationItem('Environments/DictTomcatProduction', 'udm.Dictionary', {'entries':{'tomcat.DataSource.username':'UserProduction','tomcat.DataSource.password':'cat'}}))
env = repository.create(factory.configurationItem('Environments/Tomcat-Production', 'udm.Environment', {'members':[host1.id, tomcat1.id, vh1.id,host2.id, tomcat2.id, vh2.id ], 'dictionaries':[data.id, common.id]}))
deployit.print(env)

