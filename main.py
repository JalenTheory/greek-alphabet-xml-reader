#!/usr/bin/python
# -*- coding: utf-8 -*-


import os,sys

str = "python"
print ("hello "+str)
 
folder = '.'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.xml', '.txt')
       output = os.rename(infilename, newname)


page_array = ["page8.txt","page471.txt"]

# Open a file for writing
test = open("test.txt", "wb")

#while loop
for page in page_array:
	# Open a file
	fo = open(page, "r+")
	page = fo.read();


	#convert to txt 
	pagetext_array = page.splitlines( )


	indices = [i for i, s in enumerate(pagetext_array) if 'apos' in s]
	
	
	text_array = []

	for i in range(len(indices)):
		
		text_array.append(pagetext_array[indices[i]])
	

	#print(indices)
	#print(text_array)



	# Close opend file
	fo.close()


	for text1 in text_array:
		text1 = text1[35:-len("</e:rtfTextRep>")]

		#start = text1.index("f0\fs") + len("f0\fs")
		#end = text1.index("\par")+ len("\par")

		start = text1.index("\&apos;")+ len("\&apos;")
		end = text1.index("\par &#x0A;}")

		text1= text1[start:end]

		text1 = text1.replace('&apos;','')  
		 
		 
		text1 = text1.replace('E1','α')
		text1 = text1.replace('E2','β')
		text1 = text1.replace('E3','γ')
		text1 = text1.replace('E4','δ')
		text1 = text1.replace('E5','ε')
		text1 = text1.replace('E6','ζ')
		text1 = text1.replace('E7','η')
		text1 = text1.replace('E8','θ')
		text1 = text1.replace('E9','ι')


		text1 = text1.replace('EA','κ')
		text1 = text1.replace('EB','λ')
		text1 = text1.replace('EC','μ')
		text1 = text1.replace('ED','ν')
		text1 = text1.replace('EE','ξ')
		text1 = text1.replace('EF','ο')


		text1 = text1.replace('F0','π')
		text1 = text1.replace('F1','ρ')
		text1 = text1.replace('F3','σ')
		text1 = text1.replace('F2','ς')
		text1 = text1.replace('F4','τ')
		text1 = text1.replace('F5','υ')
		text1 = text1.replace('F6','φ')
		text1 = text1.replace('F7','χ')
		text1 = text1.replace('F8','ψ')
		text1 = text1.replace('F9','ω')


		text1 = text1.replace('C7','Η')
		text1 = text1.replace('DE','ή')
		text1 = text1.replace('DC','ά')
		text1 = text1.replace('DF','ί')
		text1 = text1.replace('FE','ω')

		text1 = text1.replace('FD','ύ')
		text1 = text1.replace('DD','έ')
		text1 = text1.replace('C1','A')
		text1 = text1.replace('CC','M')
		text1 = text1.replace('C5','E')

		text1 = text1.replace('CB','Λ')
		text1 = text1.replace('D0','Π')
		text1 = text1.replace('D3','Σ')

		text1 = text1.replace("\\",'')
		text1 = text1.replace("f1lang2057",'')
		text1 = text1.replace("&quot;",'\"')

		print(text1)

		test.write( "\n\n\n" + text1);


# Close opend file
test.close()
