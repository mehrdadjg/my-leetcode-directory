from string import digits, ascii_lowercase as lowercase

class Solution:
    def getEncodedTokenAt(self, encoded, start):
        result = ''
        
        current = start
        while encoded[current] != '[':
            result += encoded[current]

            current += 1
        
        result += encoded[current]
        starting_bracket_counter = 1
        current += 1

        while starting_bracket_counter != 0:
            if encoded[current] == '[':
                starting_bracket_counter += 1
            elif encoded[current] == ']':
                starting_bracket_counter -= 1
            
            result += encoded[current]
            
            current += 1
        
        return result
    
    def parseEncodedToken(self, token):
        k = ''

        current = 0
        while token[current] != '[':
            k += token[current]

            current += 1
        
        inside_encoded = token[current + 1:-1]

        return (int(k), inside_encoded)
    
    def getPlainTokenAt(self, encoded, start):
        result = ''

        current = start
        while current < len(encoded) and encoded[current] in lowercase:
            result += encoded[current]

            current += 1
        
        return result

    def tokenizeEncodedString(self, encoded):
        result = []

        start = 0
        while start < len(encoded):
            if encoded[start] in digits:
                token = self.getEncodedTokenAt(encoded, start)
            elif encoded[start] in lowercase:
                token = self.getPlainTokenAt(encoded, start)
            
            start += len(token)
            result.append(token)
        
        return result

    def decodeString(self, encoded):
        result = ''

        tokens = self.tokenizeEncodedString(encoded)

        for token in tokens:
            if token[0] in lowercase:
                result += token
            else:
                (k, inside_encoded) = self.parseEncodedToken(token)
                inside_decoded = self.decodeString(inside_encoded)

                result += (k * inside_decoded)
        
        return result


s = Solution()
print(s.decodeString('2[abc]3[cd]ef'))