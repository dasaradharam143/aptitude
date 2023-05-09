import math


def calculateEmi(p, r, n):
    c = (1 - math.pow(r, n)) / (1 - r)
    return p / (1 + c)


def getSalary(month):
    for salary in salaries:
        startMonth = salary[0]
        endMonth = salary[1]
        if (month >= startMonth and month <= endMonth):
            return salary[2]


def getIncome(month):
    for income in incomes:
        startMonth = income[0]
        endMonth = income[1]
        if (month >= startMonth and month <= endMonth):
            return income[2] * 160 * dollar_rate


def getTrainingCost(month):
    if (month > training_payments_month):
        return 0
    else:
        result = training_cost_total
        d = training_cost_payment_month - month
        for i in range(d):
            result = result / monthly_compounding_interest
        return result


monthly_compounding_interest = 1.02
training_cost_total = 2500000
training_cost_payment_month = 60
salaries = [[0, 6, 35000], [7, 12, 60000], [13, 24, 80000], [25, 60, 120000]]
incomes = [[0, 12, 7], [13, 24, 8], [25, 29, 10], [30, 60, 13]]
training_payments_month = 60
dollar_rate = 80

totalSalary = 0
totalIncome = 0
totalTrainingCost = 0
for i in range(1, training_cost_payment_month + 1):
    monthlySalary = getSalary(i)
    monthlyIncome = getIncome(i)
    trainingCost = getTrainingCost(i)
    totalSalary = totalSalary * monthly_compounding_interest + monthlySalary
    totalIncome = totalIncome * monthly_compounding_interest + monthlyIncome
    # totalTrainingCost = totalTrainingCost * monthly_compounding_interest  # ({math.ceil(totalTrainingCost)})

    print(
        f'{i}= mSalary= {monthlySalary}, tSalary= ({math.ceil(totalSalary)})  mIncome= {monthlyIncome}, tIncome= ({math.ceil(totalIncome)}) trainingCost= {math.ceil(trainingCost)} ',end=' ')
    if (totalSalary + trainingCost) < totalIncome:
        print(f'You will be fully paid on month {i}')
        break
    else:
        x = (totalSalary + trainingCost) - totalIncome
        print(f'balanceleft {math.ceil(x)}')