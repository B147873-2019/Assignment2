﻿

#--------------------#
#---import mudules---#
#--------------------#

import subprocess
import os


#-------------------#
#----input stuff----#
#-------------------#

print('\n')
print('\n')
print('--------------Input Section--------------')
input_taxonomy_group=input('Please input the name of taxonomic group: \n' )
##loop to make sure the input is not nothing nor a number
while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
	input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
	if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
		break
print('\n')
input_protein_family=input('Please input the name of protein: \n')
##loop to make sure the input is not nothing
while input_protein_family=='':##check if input is nothing
	input_protein_family=input('The name cannot be empty, please input again：\n')
	if input_protein_family!='':
		break
print('\n')
print('-------------Query Providing-------------')
#####choose whether to search a protein or all fields search#####
input_protein_type=input('Please choose if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
##loop to check the input format:
while input_protein_type!='sp' and input_protein_type!='ns':
	input_protein_type=input('Please choose again if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
	if input_protein_type=='sp' or input_protein_type=='ns':
		break

print('\n')
input_not_select=input('Please choose whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
##loop to check format:
while input_not_select!='y' and input_not_select!='n':
	input_not_select=input('Please choose again whether you want the sequences to be not partial and not predicted ones? Please enter y for yes or n for no:\n')
	if input_not_select=='y' or input_not_select=='n':
		break
print('\n')
print('Downloading sequences from NCBI...')
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

print('----------Conservation Analysis----------')
##ask user whether to continue
continue_one=input('Now that we have the sequences successfully downloaded, do you want to continue to do the conservation analysis? Please return in y or n:\n')

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
	os.system('clustalo -i inputseqs.fasta --distmat-out=alignment_distmat --full --force -o input_seq_alignment.fasta')#make a multiple sequence alignment fistly to make preparation for cons input
	os.system('cons -sequence input_seq_alignment.fasta -outseq cons.fasta')#generate an original conservation sequence of all downloaded sequences
	print('Please wait while we are making blast database')
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
	os.system('clustalo -i best_alignment.fasta --distmat-out=alignment_distmat --full --force --percent-id')
	os.system('plotcon -sequence input_seq_alignment.fasta -winsize 4 -graph svg')
	distmat=open('alignment_distmat').read()
	len=len(distmat.split('\n'))
	distmat=distmat.split('\n')[1:len-1]#filter the useful lines of distmat which now have len-2 lines
	total=0.0
	for i in range(0,len-2):#seperate by line
		for num in range(1,len-2):
			 total=total+float(distmat[i].split()[num])
	average=total/(float(len-2)*float(len-2))
	##tell user where to find the output file
	print('Conservation sequence, distance matrix,and plot of alignment has succefully been generated in conservation.fasta,alignment_distmat,plotcon.svg and polydot.svg in your directory right now.')
	print('The level of conservation is '+str(average))
	

#------------------------------------------------#
#----task 2:scan motifs from PROSITE database----#
#------------------------------------------------#
print('-------------Motif Scanning-------------')
##ask user whether to continue
continue_two=input('Do you want to scan your sequences for motifs? Please return in y or n:\n')

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
	names=[]
	del len#we used len as a variable in task1 so now it need to be deleted
	rawseq=open('inputseqs.fasta').read()
	rawseq=rawseq.split('>')
	length=len(rawseq)
	for test in range(1,length):
		names.append(rawseq[test].split(' ')[0])
	names=set(names)
	for name in names:
		os.system('efetch -db protein -format gb -id '+name+' > genbank_format_seqs/'+name+'.gb')
		os.system('patmatmotifs -sequence genbank_format_seqs/'+name+'.gb -outfile patmatmotif/'+name+'.patmatmotifs')
		

	print('The files containing motifs of sequences are in the patmatmotif folder. Please click whichever file to see the sequence motif informations.')
		
		


#----------------------------------#
#----task3:other choices(tree/)----#
#----------------------------------#
print('--------Multiple Local Alignment--------')
continue_three=input('Do you want to have a local multiple alignment of sequences? Please return in y for yes or n for no:\n')
while continue_three.lower()!='y' and continue_three.lower()!='n':
	continue_three=input('Do you want to see the guide tree? Please return in y or n:\n')
	if continue_three.lower()=='y' or continue_three.lower()=='n':
		break
if continue_three.lower()=='y':
	os.system('edialign -sequences inputseqs.fasta -outfile local_alignment -outseq inputseqs.fasta')
	print('Successfully generated local alignment result in local_alignment')







