
#--------------------#
#---import mudules---#
#--------------------#

import subprocess
import os
import matplotlib.pyplot as plt


#-------------------#
#----input stuff----#
#-------------------#


input_taxonomy_group=input('Please input the name of taxonomic group: \n' )
##loop to make sure the input is not nothing nor a number
while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
	input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
	if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
		break

input_protein_family=input('Please input the name of protein: \n')
##loop to make sure the input is not nothing
while input_protein_family=='':##check if input is nothing
	input_protein_family=input('The name cannot be empty, please input again：\n')
	if input_protein_family!='':
		break
    

#####choose whether to search a protein or all fields search#####
input_protein_type=input('Please choose if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
##loop to check the input format:
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


#-------------------------------------------------------------------------#
#----if there are more than 10000 results or 0 results, re-input query----#
#-------------------------------------------------------------------------#

while int(how_many)>10000 or int(how_many)==0:

	os.system('rm inputseqs.fasta')#remove the former file
	if int(how_many)>10000:
		print('According the name and species you input, there are more than 10000 results......you will need to change your query: \n') 

	if int(how_many)==0:
		print('According the name and species you input, there is 0 results......you will need to change your query: \n')

	input_taxonomy_group=input('Please input the name of taxonomic group: \n' )
	##loop to make sure the input is not nothing nor a number
	while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
		input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
		if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
			break

	input_protein_family=input('Please input the name of protein: \n')
	##loop to make sure the input is not nothing
	while input_protein_family=='':##check if input is nothing
		input_protein_family=input('The name cannot be empty, please input again：\n')
		if input_protein_family!='':
			break

	input_protein_type=input('Please re-enter the type of the protein name in sp for specific or ns for non-specific: \n')
	##loop to check the input format:
	while input_protein_type!='sp' and input_protein_type!='ns':
		input_protein_type=input('Please choose again if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
		if input_protein_type=='sp' or input_protein_type=='ns':
			break

	input_not_select=input('Please re-enter whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
	##loop to check format:
	while input_not_select!='y' and input_not_select!='n':
		input_not_select=input('Please choose again whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
		if input_not_select=='y' or input_not_select=='n':
			break

	if input_protein_type.lower()=='sp'and input_not_select.lower()=='n':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
		if int(how_many)<10000 and int(how_many)!=0:
			break

	if input_protein_type.lower()=='sp' and input_not_select.lower()=='y':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
		if int(how_many)<10000 and int(how_many)!=0:
			break

	if input_protein_type.lower()=='ns'and input_not_select.lower()=='n':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 
		if int(how_many)<10000 and int(how_many)!=0:
			break

	if input_protein_type.lower()=='ns' and input_not_select.lower()=='y':
		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('rm inputseqs.fasta',shell=True)
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[All Fields] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
		if int(how_many)<10000 and int(how_many)!=0:
			break
	




#------------------------------------------------------------------------------#
#----task1:find conservation sequence, alignment matrix, and plot alignment----#
#------------------------------------------------------------------------------#


##ask user whether to continue
continue_one=input('Now that we have the sequences downloaded, do you want to continue to see the conservation sequence? Please return in y or n:\n')

##loop to check the format
while continue_one.lower()!='y' and continue_one.lower()!='n':
	continue_one=input('Please choose again whether you want the sequences to continue to see the conservation sequence? Please return in y or n:\n')
	if continue_one.lower()=='y' or continue_one.lower()=='n':
		break

#if the user want to skip task1
if continue_one.lower()=='n':
	print('OK, as you wish')

#if the user do not want to skip task1
if continue_one.lower()=='y':

	#find best 250 alignments
	os.system('cons -sequence inputseqs.fasta -outseq cons.fasta')#generate an original conservation sequence of all downloaded sequences
	os.system('makeblastdb -in inputseqs.fasta -dbtype prot -out blast_database')#make blast database with all the sequences
	os.system('blastp -db blast_database -query cons.fasta >conservation_blast_output')#use the original conservation sequence and database to blast

	#figure out the names
	best_alignment=open('conservation_blast_output').read().split('>')[0].split('(Bits)  Value\n\n')[-1].split('\n')#we only need the name part of the blast output
	best_alignment_name=[]#make a new list for top 250 sequences' names
	for num in range(0,(len(best_alignment)-2)):#the last item is nothing, so the range is not from 0 to (len()-1)
		if best_alignment[num]!='':#double check if the item is nothing
			best_alignment_name.append(best_alignment[num].split()[0])#the name (aka id number) is the first item
	best_alignment_name=best_alignment_name[0:250]#we only want the top 250 names
	##use the names we had to download 250 sequences again
	for name in best_alignment_name:
		os.system('esearch -db protein -query "'+name+'" | efetch -format fasta >> best_alignment.fasta') #use double arrow heads to add content to the end of the file

	#####this time for real--find conversation sequences:
	os.system('cons -sequence best_alignment.fasta -outseq conservation.fasta') #use cons to find conservation sequences
	os.system('polydot best_alignment.fasta -wordsize 6 -graph svg')#draw a plot of all alignments
	os.system('clustalo -i best_alignment.fasta --distmat-out=alignment_distmat --full')
	##tell user where to find the output file
	print('Conservation sequence, distance matrix,and plot of alignment has succefully been generated in conservation.fasta,alignment_distmat and polydot.svg in your directory right now.')
	


#------------------------------------------------#
#----task 2:scan motifs from PROSITE database----#
#------------------------------------------------#

##ask user whether to continue
continue_two=input('Do you want to see the results of PROSITE? Please return in y or n:\n')

##loop to check format
while continue_two.lower()!='y' and continue_two.lower()!='n':
	continue_two=input('Do you want to see the results of PROSITE? Please return in y or n:\n')
	if continue_two.lower()=='y' or continue_two.lower()=='n':
		break

#if the user want to skip task2
if continue_two.lower()=='n':
	print('OK, as you wish')

#if the user do not want to skip task2
if continue_two.lower()=='y':
	os.system('mkdir patmatmotif')
	os.system('mkdir genbank_format_seqs')
	for name in best_alignment_name:
		os.system('efetch -db protein -format gb -id '+name+' > genbank_format_seqs/'+name+'.gb')
		os.system('patmatmotifs -sequence genbank_format_seqs/'+name+'.gb -outfile patmatmotif/'+name+'.patmatmotifs')
		print('The files containing motifs of top 250 best alignment sequences are in the patmatmotif folder.')
		
		
