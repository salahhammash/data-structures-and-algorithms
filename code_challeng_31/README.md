## soulution 


def repeated_word(string):
    words = string.lower().split()
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            return word
        else:
            word_counts[word] = 1
    
    return None 





## for testing 
 text = "It was a queer, sultry summer, summer summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
 text2 ="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
 text3 = "Once upon a time, there was a brave princess who..."	 
 result = repeated_word(text2)
 print(result)    