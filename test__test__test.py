import subprocess

##input the name of taxonomic group
input_taxonomy_group=input('Please input the name of taxonomic group: \n' )
#loop to make sure the input is not nothing nor a number
while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
	input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
	if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
		break
#input the name of protein(is it a name of sepcific protein or just a rough name)
input_protein_family=input('Now please input the name of protein: \n')
#loop to make sure the input is not nothing
while input_protein_family=='':##check if input is nothing
	input_protein_family=input('The name cannot be empty, please input again：\n')
	if input_protein_family!='':
		break
    

##choose whether to search a protein or all fields search
input_protein_type=input('Now please choose if the protein name you provided (is it  a specific name (s) or a non-specific name (n))? Pleace enter s or n: \n')

while input_protein_type.lower()!='s' and input_protein_type.lower()!='n':
	input_protein_type=input('Please re-enter the type of the protein name in s or n \n')
	if input_protein_type.lower()=='s':
		how_many=subprocess.Popen('esearch -db protein -query "input_protein_family[PROT] AND input_taxonomy_group[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		print(how_many)
		break
	if input_protein_type.lower()=='n':
		how_many=subprocess.Popen('esearch -db protein -query "input_protein_family[All Fields] AND input_taxonomy_group[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		print(how_many)
		break

