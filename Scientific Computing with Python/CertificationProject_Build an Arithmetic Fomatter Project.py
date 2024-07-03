

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    #2) 정렬에 배치할 것
    firstline=""
    secondline=""
    dashes =""
    answers=""
    
    for problem in problems: #problem-한 수식뭉탱이씩
        parts=problem.split()#parts-한 뭉탱이 띄어쓰기기준
        #2)parts뭉탱이로 만든 리스트뭉치를 -> 언패킹
        operand1=parts[0]
        operator=parts[1]
        operand2=parts[2]
        
        #1) 입력 검증 수식
        if not parts[0].isdigit() or not parts[2].isdigit():#둘중에 하나라도 숫자아니면
            return "Error: Numbers must only contain digits."
        if parts[1] not in ['+','-']: # +,- 부호가 아니라면
            return "Error: Operator must be '+' or '-'."
        if len(parts[0]) > 4 or len(parts[2]) > 4: #각 뭉탱이의 길이가 4보다 크면
            return "Error: Number cannot be more than four digits."

        #3)최대길이
        max_len = max(len(operand1), len(operand2))
        width = max_len + 2
        
        #4)입력
        top = operand1.rjust(width)
        bottom = operator+" " +operand2.rjust(max_len," ")
        line = "-" * width

        #4)덧셈 뺄셈의 결과
        if show_answers:
            if operator == "+":
                result =str(int(operand1) + int(operand2)).rjust(width)
            else:
                result =str(int(operand1) - int(operand2)).rjust(width)

        #4)문제 사이에 4칸의 공백을 추가
        if problem != problems [-1]: #마지막 문제가 아닌 경우,-1는 마지막 인덱스
            #if operator == '+':
            firstline +=top+"    "
            secondline +=bottom+"    "
            dashes  +=line+"    "
            if show_answers:
                answers += result + "    " 
        else:  #마지막 문제인 경우
            firstline +=top
            secondline +=bottom
            dashes  +=line
            if show_answers:
                answers +=result
                
    #결과를 하나의 문자열로 합침
    if show_answers:
        arranged_problems = firstline + "\n"+ secondline+ "\n"+dashes +"\n"+answers
    else:
        arranged_problems = firstline + "\n"+ secondline+ "\n"+dashes 

    return arranged_problems

#sample usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))