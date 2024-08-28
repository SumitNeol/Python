def count_vowels(strings_list):
    #define vowel
    vowels='aeiouAEIOU'

    total_vowels=0
    for string in strings_list:
        count=0
        for char in string:
            if(char in vowels):
                count=count+1
        total_vowels+=count
    return total_vowels
strings_list=['hellow','world','python','programming']
print(count_vowels(strings_list))
