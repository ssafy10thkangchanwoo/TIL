T = int(input())
for tc in range(1, T+1):

    def word_reversed(word):
        for i in range((len(word)+1)//2):
            if word[i] != word[len(word)-i-1]:
                return 0
        return 1

    word = input()

    print(f'#{tc} {word_reversed(word)}')