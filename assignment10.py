# my best solution without any bug (I assume)...
#�In�some�cases,�older�people�cannot�understand�the�explanation�and�do�not�enter�1�or�0.
#�We�must�let�them�write�"Yes"�or�"No"�in�this�situations.
#�Below�codes�takes�the�answers�as�str�and�converts�them�into�bool�True�or�False
#�This�code�also�controls�invalid�entries�and�interminably�warns�the�users�
#�until�they�enter�only�"Yes"�or�"No"

while�True�:
��while�True�:��#�this�loop�continue�until�the�user�enters�"Yes"�or�"No"
����age�=�input("Are�you�a�cigarette�addict�older�than�75�years�old?\
\nPlease�enter�only�'Yes'�or�'No':�").title().strip()

����if�age�==�"Yes"�:
������age�=�True
������break
����elif�age�==�"No"�:
������age�=�False
������break
����else�:
������print("Invalid�entry!�Please�enter�only�'Yes'�or�'No")
������
��while�True�:��#�this�loop�continue�until�the�user�enters�"Yes"�or�"No"
�����chronic�=�input("Do�you�have�a�severe�chronic�disease?\
\nPlease�enter�only�'Yes'�or�'No':�").title().strip()

�����if�chronic�==�"Yes"�:
���������chronic�=�True
���������break
�����elif�chronic�==�"No"�:
��������chronic�=�False
��������break
�����else�:
��������print("Invalid�entry!�Please�enter�only�'Yes'�or�'No")
��
��while�True�:��#�this�loop�continue�until�the�user�enters�"Yes"�or�"No"
����immune�=�input("Is�your�immune�system�too�weak?\
\nPlease�enter�only�'Yes'�or�'No':�").title().strip()

����if�immune�==�"Yes"�:
������immune�=�True
������break
����elif�immune�==�"No"�:
�����immune�=�False
�����break
����else�:
������print("Invalid�entry!�Please�enter�only�'Yes'�or�'No")
����

#�Below�codes�check�whether�you�have�risk�of�death�due�to�the�coronavirus
��if�age�or�chronic�or�immune�:
���print("\nYou�are�in�the�risky�group�")
���break
��else�:
����print("\nYou�are�not�in�the�risky�group")
����break



Are you a cigarette addict older than 75 years old?
Please enter only 'Yes' or 'No': hjjk
Invalid entry! Please enter only 'Yes' or 'No
Are you a cigarette addict older than 75 years old?
Please enter only 'Yes' or 'No': no
Do you have a severe chronic disease?
Please enter only 'Yes' or 'No': hhjj
Invalid entry! Please enter only 'Yes' or 'No
Do you have a severe chronic disease?







# Solution2: Shortest code
# This code block assumes that the user always enter 1 for �Yes� and 0 for �No�
age�=�bool(int(input("Are�you�a�cigarette�addict�older�than�75�years�old?\
��\nPlease�enter�1�for�Yes�and�0�for�No:�")))

chronic�=�bool(int(input("Do�you�have�a�severe�chronic�disease?\
��\nPlease�enter�1�for�Yes�and�0�for�No:�")))

immune�=�bool(int(input("Is�your�immune�system�too�weak?\
��\nPlease�enter�1�for�Yes�and�0�for�No:�")))

if�age�or�chronic�or�immune�:
��print("You�are�in�the�risky�group�")

else�:
��print("You�are�not�in�the�risky�group")


Are you a cigarette addict older than 75 years old?  
Please enter 1 for Yes and 0 for No: 1
Do you have a severe chronic disease?  
Please enter 1 for Yes and 0 for No: 0
Is your immune system too weak?  
Please enter 1 for Yes and 0 for No: 0
You are in the risky group

Are you a cigarette addict older than 75 years old?  
Please enter 1 for Yes and 0 for No: 0
Do you have a severe chronic disease?  
Please enter 1 for Yes and 0 for No: 0
Is your immune system too weak?  
Please enter 1 for Yes and 0 for No: 0
You are not in the risky group

Are you a cigarette addict older than 75 years old?  
Please enter 1 for Yes and 0 for No: 0
Do you have a severe chronic disease?  
Please enter 1 for Yes and 0 for No: 1
Is your immune system too weak?  
Please enter 1 for Yes and 0 for No: 0
You are in the risky group
