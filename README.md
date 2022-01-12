# Get-Spelling-Sequence
Letters has one or two phonemes and are not easily understood by spelling for human and machines that are listening on the other line. In order to capture the letters spelled correctly saying the letter followed by a word increase acccuracy by captuaring the first letter in the word which has more phonemes with higher accuracy. 
The purpose of this package is to find a spelling sequence coming from a conversation.   

# Pre-Requirements
- Symbl appSecret and appId - If you don't have a Symbl account for signup look it up in this [Link](https://platform.symbl.ai/#/signup?utm_source=get-info&utm_medium=guy&utm_campaign=rep).
- Orignal recorded file was processed in Symbl using Async Audio/Video API that was completed and generated a conversationId
- The participant who spelled the word sequence will do it either by using the structure letter as in word or letter like word. For example A like apple, B as in Boy. 

# How does this work?
1. The script will use the messages API with "verbose=true" to get a JSON response with the messages word level.
2. Each word in the sequense will look for "as in" or "like" and print the letter of the word that follows it. 

# How to use?
1. Download by using the command ```git clone https://github.com/symblai/Get-Spelling-Sequence```.
2. Get into the downloaded folder using the command ```cd Get-Spelling-Sequence```.
3. Add to ```.env``` your Symbl ```APP_ID``` and ```APP_SECRET``` and save the file.
4. Open ```createSpeakerEvents.py``` and modify ```fileName``` path and ```conversationId```.
5. Run the file ```python createSpeakerEvents.py``` and in case of success this message will be generated from PUT Speakers API: ```message":"Speaker events associated for conversationId: <ConversationId Value> successfully! The update should be reflected in all messages and insights along with this conversation``` 
6. Check the results using message API [Link](https://docs.symbl.ai/docs/conversation-api/messages) or by using a POST Video Summary UI [Link](https://docs.symbl.ai/docs/api-reference/experience-api/post-video-summary-ui) with the same conversationId. 
