import boto
from boto import ec2

connection=ec2.connect_to_region("us-west-2",aws_access_key_id='AKIAJMQFFAE4HR4XMYDA',aws_secret_access_key='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')
reservations=connection.get_all_instances();
for res in reservations:
	for inst in res.instances:
    		if 'Web' in inst.tags['Name']:  
     			if inst.state=="running":
      				print "%s" % (inst.ip_address)
				with open("inventory", "r") as in_file:
      					buf = in_file.readlines()

     				with open("inventory", "w") as out_file:
      					for line in buf:
        					out_file.write(line)
        					if '[web]' in line:
  	 						out_file.write("\n%s" % (inst.ip_address))

		elif 'LB' in inst.tags['Name']:
                        if inst.state=="running":
                                print "%s" % (inst.ip_address)
                                with open("inventory", "r") as in_file:
                                        buf = in_file.readlines()

                                with open("inventory", "w") as out_file:
                                        for line in buf:
                                                out_file.write(line)
                                                if '[lb]' in line:
                                                        out_file.write("\n%s" % (inst.ip_address))

