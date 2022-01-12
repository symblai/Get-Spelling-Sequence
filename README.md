# Get-Spelling-Sequence
The purpose of this package is to find a spelling sequence coming from a conversation.
Letters phonemes are limited and are not easily understood by spelling a sequence of a word to humans or machines that are listening on the other line. In order to capture the letters spelled correctly saying the letter followed by a word increase acccuracy by captuaring the first letter in the word which has more phonemes with higher accuracy. 
   
# Pre-Requirements
- Symbl appSecret and appId - If you don't have a Symbl account for signup look it up in this [Link](https://platform.symbl.ai/#/signup?utm_source=get-info&utm_medium=guy&utm_campaign=rep).
- Orignal recorded file was processed in Symbl using Async Audio/Video API that was completed and generated a conversationId
- The participant who spelled the word sequence will do it either by using the structure ```<letter> as in <word>``` or ```<letter> like <word>```. For example "A like apple", "B as in Boy". 

# How does this work?
1. The script will use the messages API with "verbose=true" to get a JSON response with the messages word level.
2. Each word in the sequense will look for "as in" or "like" and print the letter of the word that follows it. 

# How to use?
1. Download by using the command ```git clone https://github.com/symblai/Get-Spelling-Sequence```.
2. Get into the downloaded folder using the command ```cd Get-Spelling-Sequence```.
3. Add to ```.env``` your Symbl ```APP_ID``` and ```APP_SECRET``` and save the file.
4. Open ```index.py```, modify ```conversationId``` and save the new changes. 
5. Run the file ```python index.py``` and if found the spelled letter sequence will be printed.
