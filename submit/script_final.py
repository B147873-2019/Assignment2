

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
input_not_select=input('Please choose whether you want the sequences to be not partial and not predicted ones? Please enter corresponding number: \n1 for not predicted and not partial\n2 for predicted only\n3 for partial only\n4 for both predicted and partial :\n')
##loop to check format:
while input_not_select!='1' and input_not_select!='2' and input_not_select!='2'and input_not_select!='3' and input_not_select!='4':
	input_not_select=input('Please choose again whether you want the sequences to be not partial and not predicted ones? Please enter corresponding number: \n1 for not predicted and not partial\n2 for predicted only\n3 for partial only\n4 for both predicted and partial :\n')
	if input_not_select=='1' or input_not_select=='2' or input_not_select=='3' and input_not_select=='4':
		break

print('\n')
print('Downloading sequences from NCBI...')
#####if the input is what we wanted, show the number of sequences and download them into a fasta file
if input_protein_type.lower()=='sp' and input_not_select=='1':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select=='1':
	how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

if input_protein_type.lower()=='sp' and input_not_select=='4':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select=='4':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 

if input_protein_type.lower()=='sp' and input_not_select=='2':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select=='2':
	how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

if input_protein_type.lower()=='sp' and input_not_select=='3':
	how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
if input_protein_type.lower()=='ns' and input_not_select=='3':
	how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
	how_many=str(how_many).replace("\\n'","").replace("b'",'')
	print('Now we have '+how_many+' sequences. Downloading sequences...')
	subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)


#-------------------------------------------------------------------------#
#----if there are more than 10000 results or 0 results, re-input query----#
#-------------------------------------------------------------------------#

while int(how_many)>10000 or int(how_many)==0:

	
	if int(how_many)>10000:
		os.system('rm inputseqs.fasta')#remove the former file
		print('According the name and species you input, there are more than 10000 results......you will need to change your query: \n') 

	if int(how_many)==0:
		print('According the name and species you input, there is 0 results......you will need to change your query: \n')

	print('\n')
	input_taxonomy_group=input('Please re-input the name of taxonomic group: \n' )
	##loop to make sure the input is not nothing nor a number
	while input_taxonomy_group=='' or input_taxonomy_group.isdigit(): ##check if there is nothing in input
		input_taxonomy_group=input('The group name can not be nothing, and can only be a alphabetic word! Please input again: \n' )
		if input_taxonomy_group!='' and input_taxonomy_group.isalpha(): ##progress under the condition that the taxonomy group's name isn't nothing
			break
	print('\n')
	input_protein_family=input('Please re-input the name of protein: \n')
	##loop to make sure the input is not nothing
	while input_protein_family=='':##check if input is nothing
		input_protein_family=input('The name cannot be empty, please input again：\n')
		if input_protein_family!='':
			break
	print('\n')
	input_protein_type=input('Please re-enter the type of the protein name in sp for specific or ns for non-specific: \n')
	##loop to check the input format:
	while input_protein_type!='sp' and input_protein_type!='ns':
		input_protein_type=input('Please choose again if the protein name you provided (is it a specific name (sp) or a non-specific name (ns))? Pleace enter sp or ns: \n')
		if input_protein_type=='sp' or input_protein_type=='ns':
			break
	print('\n')
	
	input_not_select=input('Please choose whether you want the sequences to be not partial and not predicted ones? Please enter corresponding number: \n1 for not predicted and not partial\n2 for predicted only\n3 for partial only\n4 for both predicted and partial :\n')
	##loop to check format:
	while input_not_select!='1' and input_not_select!='2' and input_not_select!='2'and input_not_select!='3' and input_not_select!='4':
		input_not_select=input('Please choose again whether you want the sequences to be not partial and not predicted ones? Please enter corresponding number: \n1 for not predicted and not partial\n2 for predicted only\n3 for partial only\n4 for both predicted and partial :\n')
		if input_not_select=='1' or input_not_select=='2' or input_not_select=='3' and input_not_select=='4':
			break


	if input_protein_type.lower()=='sp' and input_not_select=='1':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
	if input_protein_type.lower()=='ns' and input_not_select=='1':
		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

	if input_protein_type.lower()=='sp' and input_not_select=='4':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
	if input_protein_type.lower()=='ns' and input_not_select=='4':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism]" | efetch -format fasta > inputseqs.fasta',shell=True) 

	if input_protein_type.lower()=='sp' and input_not_select=='2':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
	if input_protein_type.lower()=='ns' and input_not_select=='2':
		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Predicted[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

	if input_protein_type.lower()=='sp' and input_not_select=='3':
		how_many=subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True)
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[PROT] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)
	
	if input_protein_type.lower()=='ns' and input_not_select=='3':
		how_many=(subprocess.check_output('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta |grep ">" | wc -l',shell=True))
		how_many=str(how_many).replace("\\n'","").replace("b'",'')
		print('Now we have '+how_many+' sequences. Downloading sequences...')
		subprocess.Popen('esearch -db protein -query "'+input_protein_family+'[Ti] AND '+input_taxonomy_group+'[Organism] NOT Partial[All Fields]" | efetch -format fasta > inputseqs.fasta',shell=True)

	




#------------------------------------------------------------------------------#
#----task1:find conservation sequence, alignment matrix, and plot alignment----#
#------------------------------------------------------------------------------#
print('\n')
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
	
	print('OK, cover that! Please wait in patience!')
	if int(how_many) > 250:

		#find best 250 alignments
		os.system('clustalo -i inputseqs.fasta --full --force -o input_seq_alignment.fasta')#make a multiple sequence alignment fistly to make preparation for cons input
		os.system('cons -sequence input_seq_alignment.fasta -outseq cons.fasta')#generate an original conservation sequence of all downloaded sequences
		print('Now we are making blast database, please keep waiting...')
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
	
		#####this time for real--find conversation sequences, using the top 250 ones
		os.system('clustalo -i best_alignment.fasta --distmat-out=alignment_distmat --full --force -o input_best_alignment.fasta')#multiple alignment first
		os.system('cons -sequence input_best_alignment.fasta -outseq conservation_output/conservation.fasta') #use cons to find conservation sequences
		os.system('polydot input_best_alignment.fasta -wordsize 6 -graph svg')#draw a plot of all alignments
		os.system('clustalo -i best_alignment.fasta --distmat-out=alignment_percentage --full --force --percent-id')
		os.system('plotcon -sequence input_best_alignment.fasta -winsize 4 -graph svg')#the input of plotcon can only be aligned sequences
		distmat=open('alignment_percentage').read()
		leng=len(distmat.split('\n'))
		distmat=distmat.split('\n')[1:leng-1]#filter the useful lines of distmat which now have leng-2 lines
		total=0.0
		for i in range(0,leng-2):#seperate by line
			for num in range(1,leng-2):
			 	total=total+float(distmat[i].split()[num])
		average=total/(float(leng-2)*float(leng-2))
		
	if int(how_many) <= 250:
		os.system('clustalo -i inputseqs.fasta --distmat-out=alignment_distmat --full --force -o input_seq_alignment.fasta')#multiple alignment
		os.system('cons -sequence input_seq_alignment.fasta -outseq conservation.fasta') #use cons to find conservation sequences
		os.system('polydot input_seq_alignment.fasta -wordsize 6 -graph svg')#draw a plot of all alignments
		os.system('clustalo -i inputseqs.fasta --distmat-out=alignment_percentage --full --force --percent-id')
		os.system('plotcon -sequence input_seq_alignment.fasta -winsize 4 -graph svg')
		distmat=open('alignment_percentage').read()
		leng=len(distmat.split('\n'))
		distmat=distmat.split('\n')[1:leng-1]
		total=0.0
		for i in range(0,leng-2):#seperate by line
			for num in range(1,leng-2):
			 	total=total+float(distmat[i].split()[num])
		average=total/(float(leng-2)*float(leng-2))
	##tell user where to find the output file
	print('-----Outputs-----')
	print('Conservation sequence, distance matrix, percentage matrix ,and plot of conservation and alignment has succefully been generated in conservation.fasta,alignment_distmat, alignment_percentage,plotcon.svg and polydot.svg in your directory right now.')
	print('The degree of similarity is '+str(average))



#------------------------------------------------#
#----task 2:scan motifs from PROSITE database----#
#------------------------------------------------#
print('\n')
print('-------------Motif Scanning-------------')
##ask user whether to continue
continue_two=input('Do you want to scan your sequences for motifs? Please return in y or n:\n')

##loop to check format
while continue_two.lower()!='y' and continue_two.lower()!='n':
	continue_two=input('Do you want to see the results of PROSITE? Please return in y or n:\n')
	if continue_two.lower()=='y' or continue_two.lower()=='n':
		break

def save_to_file(file_name,contents):
    f = open('file_name','w')
    f.write(contents)
    f.close()

#if the user want to skip task2
if continue_two.lower()=='n':
	print('OK, as you wish')

#if the user do not want to skip task2
if continue_two.lower()=='y':
	print('Please wait while the sequences are scanned one by one...')
	os.system('mkdir patmatmotif')
	os.system('mkdir genbank_format_seqs')
	names=[]
	
	rawseq=open('inputseqs.fasta').read()
	rawseq=rawseq.split('>')
	length=len(rawseq)
	for test in range(1,length):
		names.append(rawseq[test].split(' ')[0])
	names=set(names)
	print('The brief information of motifs will show on the screen while the sequences be processed: ')
	for name in names:
		os.system('efetch -db protein -format gb -id '+name+' > genbank_format_seqs/'+name+'.gb')#download genbank format sequences
		os.system('patmatmotifs -sequence genbank_format_seqs/'+name+'.gb -outfile patmatmotif/'+name+'.patmatmotifs')#use patmatmotif to analyse
		file=open('patmatmotif/'+name+'.patmatmotifs').read()#open file
		hitcount=int(file.split('# HitCount: ')[1].split('\n#')[0])#calculate hitcount
		if hitcount==0:
			motif='-'
		if hitcount!=0:
			motif=''
			for i in range(1,hitcount+1):
				motif=motif+' '+file.split('Motif = ')[i].split('\n')[0]
		save_to_file('patmatmotif/motif',str(name))
		save_to_file('patmatmotif/motif',str(hitcount))
		save_to_file('patmatmotif/motif',str(motif))
		print(name,'\t',hitcount,'\t',motif)
	print('\n')
	print('-----Outputs-----')
	print('The files containing motifs of sequences are in the patmatmotif folder.And the summary is in "motif" in the patmatmotif folder. Please click whichever file to see the sequence motif informations.')
		
		


#----------------------------------#
#-------task3:other choices--------#
#----------------------------------#


print('\n')
print('--------Information of Alignment--------')
continue_five=input('Do you want to see the basic information of the multiple alignment? Please return in y for yes or n for no:\n')
while continue_five.lower()!='y' and continue_five.lower()!='n':
	continue_five=input('Do you want to see the basic information of the multiple alignment? Please re-enter in y or n:\n')
	if continue_five.lower()=='y' or continue_five.lower()=='n':
		break
if continue_five.lower()=='n':
	print('OK, as you wish')
if continue_five.lower()=='y':
	print('Please wait while the basic information of the multiple alignment are generating...')
	os.system('infoalign -sequence input_seq_alignment.fasta -outfile information_of_alignment')
	print('Successfully generated basic information of the multiple alignment in information_of_alignment')


print('\n')
print('--------Display Alignment--------')
continue_six=input('Do you want to see the display of the multiple alignment? Please return in y for yes or n for no:\n')
while continue_six.lower()!='y' and continue_six.lower()!='n':
	continue_six=input('Do you want to see the display of the multiple alignment? Please re-enter in y or n:\n')
	if continue_six.lower()=='y' or continue_six.lower()=='n':
		break
if continue_six.lower()=='n':
	print('OK, as you wish')
if continue_six.lower()=='y':
	print('Please wait while the display of the multiple alignment are generating...')
	os.system('showalign -sequence input_seq_alignment.fasta -outfile display_of_alignment')
	print('Successfully generated display of the multiple alignment in display_of_alignment')

print('\n')
print('--------Multiple Local Alignment--------')
continue_three=input('Do you want to have a local multiple alignment of sequences? Please return in y for yes or n for no:\n')
while continue_three.lower()!='y' and continue_three.lower()!='n':
	continue_three=input('Do you want to see local multiple alignment result? Please re-enter in y or n:\n')
	if continue_three.lower()=='y' or continue_three.lower()=='n':
		break
if continue_three.lower()=='n':
	print('OK, as you wish')
if continue_three.lower()=='y':
	print('Please wait while the local alignment of sequences are generating...')
	os.system('edialign -sequences inputseqs.fasta -outfile local_alignment -outseq inputseqs.fasta')
	print('Successfully generated local alignment result in local_alignment')



print('\n')
print('----Ambiguous Conservation Sequence-----')
continue_four=input('Do you want to have an ambiguous conservation sequence of sequences? Please return in y for yes or n for no:\n')
while continue_four.lower()!='y' and continue_four.lower()!='n':
	continue_four=input('Do you want to see the ambiguous conservation sequence? Please re-enter in y or n:\n')
	if continue_four.lower()=='y' or continue_four.lower()=='n':
		break
if continue_four.lower()=='n':
	print('OK, as you wish')
if continue_four.lower()=='y':
	print('Please wait while the ambiguous conservation sequence are generating...')
	os.system('consambig -sequence input_seq_alignment.fasta -outseq')
	print('Successfully generated ambiguous conservation sequence in local_alignment')






