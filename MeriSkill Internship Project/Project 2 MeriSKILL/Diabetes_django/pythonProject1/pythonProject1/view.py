import pandas as pd
def result(request):
    data = pd.read_csv("C:\pythonProject1\diabetes.csv")
    X = data.drop (labels: "outcome", axis=1),
    Y = data("outcome")
    X_train,X_test,Y_train,Y_test = train_test_split(*arrays, X,Y,test_size=0.2)


    model= LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pared = model.predict([val1, val2, val3, val4, val5, val6, val7, val8])

    result = ""

    if pared == [1]:
        result1 = "postive1"
    elif pared == [0]:
        result1 = "negative"

    return render(request, template_name:"predict.html", context: {"result2":result})