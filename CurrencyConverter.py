import tkinter as tk
import tkinter.ttk as ttk
import requests


# https://v6.exchangerate-api.com/v6/api_keys/pair/USD/NGN
base_url = "https://v6.exchangerate-api.com/"

def convert_pressed():
    amount= input_text.get()
    from_curr= source_value.get()
    to_curr= target_value.get()
    main_url= base_url + "v6/keys/pair/" + from_curr + "/" + to_curr

#     main_url1= base_url + "v6/keys/pair/" + from_curr + "/" + to_curr
    req= requests.get(main_url)
    result= req.json()
    if result['result'] == 'success':
        conversion_rate = result['conversion_rate']
        converted_amount = float(amount) * conversion_rate
        conversion_label.config(text=f"{amount} {from_curr}"
                                     f" = {converted_amount:.2f} {to_curr}")
    else:
        conversion_label.config(text="Error in fetching conversion rate")


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title("MUNICH™ FX")
    main_window.geometry("350x200")

    intro_label = tk.Label(main_window, text="Welcome to Munich Fx",
                           fg="white", bg="blue", relief=tk.RAISED, borderwidth=3)
    intro_label.config(font=("Courier", 10, "bold"))
    main_window.grid_columnconfigure(0, weight=1)
    intro_label.grid(row=1)

    input_text = tk.StringVar()
    currency_field = tk.Entry(main_window, justify="right", textvariable=input_text)
    currency_field.grid(row=2, padx=5, pady=5)

    country_code = ["USD", "NGN", "GBP", "CAD", "EUR"]
    source_value = tk.StringVar()
    source_value_selection = ttk.Combobox(main_window, values=country_code,
                                          textvariable=source_value)
    source_value_selection.current(0)
    source_value_selection.grid(row=3)

    target_value = tk.StringVar()
    target_value_selection = ttk.Combobox(main_window, values=country_code,
                                          textvariable=target_value)
    target_value_selection.current(1)
    target_value_selection.grid(row=4)

    convert_button = tk.Button(main_window, text="Convert", height=1, width=7,
                               command=lambda: convert_pressed())
    convert_button.grid(row=5)

    conversion_label = tk.Label(text="")
    conversion_label.grid(row=6)

    main_window.mainloop()
