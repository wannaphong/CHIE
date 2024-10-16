system_prompt='''Please evaluate these answers based on their accuracy and relevance to the provided passage that based on the Criteria:
1. The Answer is Correct concerning the Reference Answer. Do you agree or disagree?
Determine if the given answer accurately matches the reference answer provided. The correctness here means the answer must directly correspond to the reference answer, ensuring factual accuracy.
2. The Answer Includes Relevant, Additional Information from the Context. Do you agree or disagree?
Assess whether the answer provides extra details that are not only correct but also relevant and enhance the understanding of the topic as per the information given in the context.
3. The Answer Includes Additional, Irrelevant Information from the Context. Do you agree or disagree?
Check if the answer contains extra details that, while related to the context, do not directly pertain to the question asked. This information is not necessary for answering the question and is considered a digression.
4. The Answer Includes Information Not Found in the Context. Do you agree or disagree?
Evaluate if the answer includes any information that is not included in the context. This information, even if correct, is extraneous as it goes beyond the provided text and may indicate conjecture or assumption.'''

model_name="gpt-4"
import re
def get_point(text):
    s=re.findall(r"(\d) (point|Point)", text)[0]
    #s=re.findall(r"\d", s)[0]
    return int(s[0])
    # except:
    #     return None

def change_yes_no(p):
    return "Agree" in p
def get_bool(text):
    s=re.findall(r"(Disagree|Agree)", text)
    #print(s)
    #return s
    #s=re.findall(r"\d", s)[0]
    if len(s) != 4:
        return None
    
    return [change_yes_no(i) for i in s]
# def score(bool_list):
#     _socre=0
#     if not bool_list[0]:
#         print(0)
#         _socre= 0
#     elif bool_list[1] and bool_list[2] and not bool_list[5]:
#         print(4)
#         _socre= 4
#     elif bool_list[1] and not bool_list[5]:
#         print(3)
#         _socre= 3
#     elif bool_list[4] and not bool_list[5]:
#         print(2)
#         _socre= 2
#     elif bool_list[5]:
#         print(1)
#         _socre= 1
#     return _socre

def score(l):
    if not l[0]: # q1 no
        return 0
    else:
        if l[3]: # q1 yes
            return 1
        else: # q4 no
            if l[1]: # q2 yes
                return 4
            elif not l[1] or not l[2]:  # q2 no and q3 no
                return 3
            elif l[2]: # q3 yes
                return 2