#Assignment2

#input_help=input('Would you like to see the help menual? -in Y or N\n\t')
#	if input_help.upper()=='Y':
#	imput_user=input('Are you an ordinary user -in 1 or a competent Python3 code-writer?\n\t')
#		if input_user=='1':
#			open('ordinary_user.txt').read()
#		if input_user=='2':
#			open('python.txt').read()


#input the name of protein's family
input_protein_family=input('Please input the name of protein family you wish to study: \n\t')

#check if input is nothing
if len(input_protein_family)=='0':
    input_protein_family=input('The name cannot be empty, please input again \n\t')
    
#split input by space and make it a list
ipf=(input_protein_family).split(' ')

#check if the input is a name of protein  
if ipf[-1]!='protein':
    input_protein_family=input('the name must be a protein! Please input again \n\t')
    
#check if the input is just 'protein'
if input_protein_family.lower()=='protein':
    input_protein_family=input('You got me! Now please input a real protein! \n\t')
    

#input the name of taxonomic group
input_taxonomy_group=input('Please input the name of taxonomic group: \n\t' )

if input_taxonomy_group=='':
    input_taxonomy_group=input('The group name cannot be empty! Please input again: \n\t' )
    

#"glucose-6-phosphatase"[PROT] AND "aves"[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]

print('I am searching protein sequences under protein family of ',input_protein_family,' in ',input_taxonomy_group)
print('1 second please')
import subprocess

#call
subprocess.Popen('esearch -db protein -query "glucose-6-phosphatase[PROT] AND aves[Organism] NOT Predicted[All Fields] NOT Partial[All Fields]" | efetch -format fasta >inputseqs.fasta',shell=True)

how_many=subprocess.Popen('cat inputseqs.fasta|grep ">"|wc -l',shell=True)

print('successfully downloaded ',how_many,' sequences from NCBI, and saved them in inputseqs.fasta')



decide_con=input('Would you like to see the conservation sequence among these sequences?(in Y or N)\n\t')
if decide_con.upper()=='Y':


	subprocess.Popen('cons -sequence inputseqs.fasta -outseq cons.fasta',shell=True)

	subprocess.Popen('consambig -sequence inputseqs.fasta -outseq consambig.fasta',shell=True)
	print('both conservation sequence and ambiguity conservation sequende is now finished processing')
	decide_conresult=input('Would you like to see the results?(in Y or N)\n\t')
	if decide_conresult.upper()=='Y':
		open('cons.fasta').read()
	input_polydot=input('Would you like to see the rough alignment picture?(in Y or N)\n\t')
	if input_polydot.upper()=='Y': 
		subprocess.Popen('polydot inputseqs.fasta -wordsize 6 -graph svg',shell=True)


