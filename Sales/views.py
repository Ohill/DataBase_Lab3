from lxml import etree
from django.shortcuts import render
from .forms import *
from .table import Fact_Sale_Table
from django_tables2 import RequestConfig
from Site.table import Site_Table
from Team.table import Team_Table
from  Customer.table import Customer_Table
from django.db import connection
from .models import *
from django.db.models import Q
import re


def Sales(request):

    form_fact_sales =  Fact_Sales_Form(request.POST or None)
    table = table_view(request)
    table_site = table_site_(request)
    table_team = table_team_(request)
    stored_proc_tbl = stored_proc(request)
    table_customer = table_customer_(request)
    backup_tbl = backup_table(request)
    form_id = Fact_Sales_Form_ID(request.POST or None)
    trigger = Trigger_Form(request.POST or None)
    upload_form = Upload_Form(request.POST or None)
    form_dpz = Site_ID_search(request.POST or None)
    form2 = Fact_Sales_Form2(request.POST or None)
    site_ctg = Site_Category_Form(request.POST or None)
    customer_id = Customer_ID_Form(request.POST or None)
    customer_name = Customer_Name_Form (request.POST or None)
    team_form = Team_Form(request.POST or None)
    return render(request, 'Sales/Sales.html', locals())


def add_data(request):
    try:
        #cursor = connection.cursor()
        #     #print("INSERT INTO db_lab2.sales_fact_sale (Date,Cost,Team_id_id,Site_id_id,Customer_id_id) VALUES ('"+request.POST['Date']+"',"+"'"+request.POST['Cost']+"','"+request.POST['Team_id']+"','"+request.POST['Site_id']+"','"+request.POST['Customer_id']+"')")
        #cursor.execute("INSERT INTO db_lab2.sales_fact_sale (Date,Cost,Team_id_id,Site_id_id,Customer_id_id) VALUES ('"+request.POST['Date']+"',"+"'"+request.POST['Cost']+"','"+request.POST['Team_id']+"','"+request.POST['Site_id']+"','"+request.POST['Customer_id']+"')")
        Fact_Sale.objects.create(Date=request.POST['Date'],  Cost=request.POST['Cost'],
                                                                  Team_id_id =request.POST['Team_id'],
                                                                  Site_id_id =request.POST['Site_id'],
                                                                  Customer_id_id =request.POST['Customer_id'])
    except:
        print("lol")
        pass
    return Sales(request)





def table_view(request):
    table = Fact_Sale_Table(Fact_Sale.objects.all())
    RequestConfig(request).configure(table)
    return table

def table_customer_(request):
    #sql_request = "select * from customer_customer"
    obj = Customer.objects.all()
    try:
        if request.POST['id_']:
            str2 = request.POST['id_']
            str1 = ''
            z = 0
            for i in str2:
                z += 1
                if i == "-":
                    str2 = str2[z:]
                    break
                str1 += i
            if (int(str1) < int(str2)):
                obj = Customer.objects.filter(Q(Customer_id__gte=int(str1)) & Q(Customer_id__lte=int(str2)))
                #sql_request = "select * from db_lab2.customer_customer where (Customer_id=>" + str1 + ") and (Customer_id<=" + str2 + ")"
    except:
        try:
            str1 = request.POST['Customer_Name']
            #str1 = "'" + str1 + "'"
            if request.POST['Customer_Name']:
                #sql_request = "select * from db_lab2.customer_customer where Customer_Name=" + str1
                obj = Customer.objects.filter(Customer_Name__contains=str1)
        except:
            pass
    table = Customer_Table(obj)
    RequestConfig(request).configure(table)
    return table

def table_team_(request):
    #sql_request = "select * from team_team"
    obj = Team.objects.all()
    try:
        if request.POST['search_in']:
            num = request.POST['search_in']
            str2 = request.POST['_']
            if num == '1':
                if (str2.isdecimal()):
                    obj = Team.objects.filter(Q(Team_id__lte=int(str2)))
                else:

                    result = re.split(r'\D',str2)
                    str1 = result[0]
                    str2 = result[-1]
                    # str1=tmp=''
                    # z = 0
                    # for i in str2:
                    #     if (i.isdecimal()) and (z == 0):
                    #         str1+=i
                    #     elif not(i.isdecimal()):
                    #         z=1
                    #     if i.isdecimal() and z == 1:
                    #         tmp+=i
                    # str2 = tmp
                    if (int(str1) < int(str2)):
                        #sql_request = "select * from db_lab2.team_team where (Team_id>" + str1 + ") and (Team_id<" + str2 + ")"
                        obj = Team.objects.filter(Q(Team_id__gte=int(str1)) & Q(Team_id__lte=int(str2)))
            elif num == '2':
                #str2= "'"+str2+"'"
                #sql_request = "select * from db_lab2.team_team where Country_id=" + str2
                obj = Team.objects.filter(Country_id=str2)
            elif num == '3':
                obj = Team.objects.filter(Characters__contains=str2)
    except:
        pass
    table = Team_Table(obj)
    RequestConfig(request).configure(table)
    return table


def table_site_(request):
    #sql_request = "select * from site_site"
    obj = Site.objects.all()
    try:
        if request.POST['id_from']:
            str2 = request.POST['id_from']
            str1=''
            z = 0
            for i in str2:
                z+=1
                if i == "-":
                    str2 = str2[z:]
                    break
                str1+=i
            if (int(str1)<int(str2)):
                #sql_request="select * from db_lab2.site_site where (Site_id>"+str1+") and (Site_id<"+str2+")"
                obj = Site.objects.filter(Q(Site_id__gte=int(str1)) & Q(Site_id__lte=int(str2)))
                print(obj)
    except:
        try:
            str1 = request.POST['Category']
            #str1="'"+str1+"'"
            if request.POST['Category']:
                #sql_request = "select * from db_lab2.site_site where Site_Category_id="+str1
                obj = Site.objects.filter(Site_Category=str1)
        except:
            pass
    #table = Site_Table(Site.objects.raw(sql_request))
    table = Site_Table(obj)
    RequestConfig(request).configure(table)
    return table


def del_sale(request):
    #db = MySQLdb.connect(host="localhost", user="root", passwd="", db="db_lab2")
    try:
        #Sales(request)
        Fact_Sale.objects.filter(id=request.POST['id_delete']).delete()
    except:

        pass
    return Sales(request)

def update_sales(request):
    try:
        Fact_Sale.objects.filter(id=request.POST['id_Update']).update(Date=request.POST['Date'], Cost=request.POST['Cost'],
                                                          Team_id=request.POST['Team_id_Update'],
                                                          Site_id=request.POST['Site_id_Update'],
                                                          Customer_id=request.POST['Customer_id_Update'])
    except:

        pass
    return Sales(request)


def upload_data(request):
    try:
        if request.POST['upload_from']:
            filename = request.POST['upload_from']
            cursor = connection.cursor()
            cursor.execute("DELETE  FROM db_lab2.sales_fact_sale where (id > 0)")
            Fact_Sale.objects.filter(id__gte=0).delete()
            def quote(text):
                return "'" + text + "'"

            def doublequote(text):
                return '"' + text + '"'

            #print(filename + ".xml")
            #file = open(filename+".xml","r")

            #file.close()
            tree = etree.parse(filename+".xml")
            root = tree.getroot()
            cursor.execute("DELETE  FROM db_lab2."+filename+"_"+filename+" where ("+filename+"_"+"id > 0)")
            filename = filename + "_" + filename
            # Parse out data from XML
            data = []
            for child in root:
                datarow = {}
                for leaf in child:
                    datarow[leaf.tag] = leaf.text
                data.append(datarow)

            # Push data to DB

            statements = []
            for row in data:
                columns = []
                values = []
                for item in row:
                    # Reformatting data to mySQL formats
                    columns.append(item.replace(" ", ""))
                    temp = row[item]
                    values.append(quote(temp.replace("'", "")))

                    # Push data to table
                statement = "INSERT INTO db_lab2." + filename + " (" + ",".join(columns) + ") VALUES (" + \
                            ",".join(values) + ")"

                statements.append(statement)

            for statement in statements:
                cursor.execute(statement)


    except:
         pass

    return Sales(request)


def stored_proc(request):
    table = Fact_Sale_Table(Fact_Sale.objects.raw('Call max_cost();'))
    RequestConfig(request).configure(table)
    return table


def backup_table(request):
    table = Fact_Sale_Table(Fact_Sale.objects.raw('SELECT * FROM db_lab2.backup'))
    RequestConfig(request).configure(table)
    return table


def work_trigger(request):

    if request.POST["Trigger"]:
        num = request.POST["Trigger"]
        if num == 1:
            try:
                cursor = connection.cursor()
                cursor.execute("""DELIMITER |
            CREATE TRIGGER `delete_sale` before delete ON `sales_fact_sale`
            FOR EACH ROW BEGIN
              INSERT INTO backup Set id =OLD.id, Date = OLD.Date, Cost = OLD.Cost, Customer_id_id = OLD.Customer_id_id, Site_id_id=OLD.Site_id_id, Team_id_id = OLD.Team_id_id;
            END""")
            except:
                pass
        elif num == 2:
            try:
                cursor = connection.cursor()
                cursor.execute("drop trigger delete_sale")
            except:
                print(request.POST)
                pass

    return Sales(request)


