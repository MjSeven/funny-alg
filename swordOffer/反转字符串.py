
s = 'i love you'
print(s[::-1])
print(''.join(list(reversed(s))))
"""
C 语言
void Reverse(char* pBegin, char* pEnd)
{
    if(pBegin == nullptr || pEnd == nullptr)
        return;
    while(pBegin < pEnd)
    {
        char temp = *pBegin;
        *Begin = *pEnd;
        *pEnd = temp;
        pBegin++, pEnd--;
    }
}
"""