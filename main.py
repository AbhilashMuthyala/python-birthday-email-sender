
import smtplib, datetime, pandas, random

def send_email(msg):
    my_email = '<email>'
    password = '<password>'
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="<to_email>",
                        msg=f"Subject: Hello \n\n {msg}")

def current_date():
    cur_time = datetime.datetime.now()
    return cur_time.month, cur_time.day

def read_quotes():
    with open('quotes.txt') as quotes_file:
        list_quotes = quotes_file.readlines()
        random_quote = random.choice(list_quotes)
        return random_quote

def random_card_pick():
    return random.randint(1,3)

def send_birthday_email():
    cur_date_param = current_date()
    with open('birthdays.csv') as birthday_file:
        birthday_list = birthday_file.readlines()[1:]
    for item in birthday_list:
        var_list = item.split(",")
        print(var_list[1])
        item_month = var_list[1]
        item_day = var_list[2]
        if int(item_month) == cur_date_param[0] and int(item_day) == cur_date_param[1]:
            random_num = random_card_pick()
            with open(f"letter_templates/letter_{random_num}.txt") as letter_selected:
                letter_selected = letter_selected.read().replace('[NAME]',f'{var_list[0]}')
                send_email(letter_selected)

if __name__ == '__main__':
    send_birthday_email()
