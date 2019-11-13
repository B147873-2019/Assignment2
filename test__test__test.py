
import subprocess

#####input the name of taxonomic group#####
input_taxonomy_group=input('Please input the name of taxonomic group: \n' )
##loop to make sure the input is not nothing nor a number
while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
	input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
	if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
		break

######input the name of protein#####
input_protein_family=input('Please input the name of protein: \n')
##loop to make sure the input is not nothing
while input_protein_family=='':##check if input is nothing
	input_protein_family=input('The name cannot be empty, please input again：\n')
	if input_protein_family!='':
		break
    

#####choose whether to search a protein or all fields search#####
input_protein_type=input('Please choose if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
##loop to check the input is in correct format:
while input_protein_type!='sp' and input_protein_type!='ns':
	input_protein_type=input('Please choose again if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
	if input_protein_type=='sp' or input_protein_type=='ns':
		break

input_not_select=input('Please choose whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
##loop to check format:
while input_not_select!='y' and input_not_select!='n':
	input_not_select=input('Please choose again whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
	if input_not_select=='y' or input_not_select=='n':
		break

#####if the input is what we wanted, show the number of sequences and download them into a fasta file
if input_protein_type.lower()=='sp' and input_not_select.lower()=='y':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select.lower()=='y':
	how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

if input_protein_type.lower()=='sp' and input_not_select.lower()=='n':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select.lower()=='n':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 

#####if the input is not what we wanted
#while input_protein_type.lower()!='sp' or input_protein_type.lower()!='ns' or input_not_select.lower()!='y' or input_not_select.lower()!='n':
#	input_protein_type=input('Please re-enter the type of the protein name in sp for specific or ns for non-specific: \n')
#	input_not_select=input('Please re-enter whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
#	if input_protein_type.lower()=='sp'and input_not_select.lower()=='n':
#		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
#		how_many=str(how_many).replace("\\n'","").replace("b'",'')
#		print('Now we have '+how_many+' sequences. Downloading sequences...')
#		subprocess.Popen('rm inputseqs.fasta',shell=True)
#		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
#		break
#
#	if input_protein_type.lower()=='sp' and input_not_select.lower()=='y':
#		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
#		how_many=str(how_many).replace("\\n'","").replace("b'",'')
#		print('Now we have '+how_many+' sequences. Downloading sequences...')
#		subprocess.Popen('rm inputseqs.fasta',shell=True)
#		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
#		break
#
#	if input_protein_type.lower()=='ns'and input_not_select.lower()=='n':
#		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
#		how_many=str(how_many).replace("\\n'","").replace("b'",'')
#		print('Now we have '+how_many+' sequences. Downloading sequences...')
#		subprocess.Popen('rm inputseqs.fasta',shell=True)
#		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 
#		break
#
#	if input_protein_type.lower()=='ns' and input_not_select.lower()=='y':
#		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
#		how_many=str(how_many).replace("\\n'","").replace("b'",'')
#		print('Now we have '+how_many+' sequences. Downloading sequences...')
#		subprocess.Popen('rm inputseqs.fasta',shell=True)
#		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
#		break
#

#####if results are too many, re-input query
while int(how_many)>10000:
	print('According the name and species you input, I have found more than 10000 results......you will need to change your query: \n') 
	input_protein_type=input('Please re-enter the type of the protein name in sp for specific or ns for non-specific: \n')
	input_not_select=input('Please re-enter whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
	if input_protein_type.lower()=='sp'and input_not_select.lower()=='n':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
		break

	if input_protein_type.lower()=='sp' and input_not_select.lower()=='y':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
		break

	if input_protein_type.lower()=='ns'and input_not_select.lower()=='n':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 
		break

	if input_protein_type.lower()=='ns' and input_not_select.lower()=='y':
		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
		break
		