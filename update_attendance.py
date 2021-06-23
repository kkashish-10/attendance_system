import csv
import os
import shutil
from tempfile import NamedTemporaryFile
from tkinter import StringVar, Label, Tk, messagebox, LabelFrame, ttk, Button, filedialog
from tkinter.constants import RIDGE, W, HORIZONTAL, VERTICAL, BOTH, END
from PIL import Image, ImageTk

my_data_rows = []


class AttendanceManager:
    def __init__(self, win_tk_root):  # constructor

        # setup for the mainframe of the window
        # window title
        self.root = win_tk_root
        self.root.title("Attendance System(Attendance Manager)")

        # get screen dimensions
        screen_width = win_tk_root.winfo_screenwidth()
        screen_height = win_tk_root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (screen_width, screen_height))  # full screen window
        self.root.resizable(False, False)  # resizable window

        # variables
        self.var_att_roll_no = StringVar()
        self.var_att_name = StringVar()
        self.var_att_department = StringVar()
        self.var_att_course = StringVar()
        self.var_att_date = StringVar()
        self.var_att_time = StringVar()
        self.var_att_status = StringVar()  # attendance status

        # setup the content of the window

        top_left_image = Image.open("project_images/img_admin_attendance.jpg")
        top_left_image = top_left_image.resize((round(screen_width * 0.5), round(0.2 * screen_height)), Image.ANTIALIAS)
        self.top_left_photo_image = ImageTk.PhotoImage(top_left_image)
        top_left_image_label = Label(self.root, image = self.top_left_photo_image)
        top_left_image_label.place(x = 0, y = 0, width = round(screen_width * 0.5), height = round(screen_height * 0.2))

        top_right_image = Image.open("project_images/img_students.jpg")
        top_right_image = top_right_image.resize((round(screen_width * 0.5), round(screen_height * 0.2)),
                                                 Image.ANTIALIAS)
        self.top_right_photo_image = ImageTk.PhotoImage(top_right_image)
        top_right_image_label = Label(self.root, image = self.top_right_photo_image)
        top_right_image_label.place(x = round(screen_width * 0.5) + 1, y = 0, width = round(screen_width / 2),
                                    height = round(screen_height * 0.2))

        title_label = Label(self.root, text = "Attendance Management (Admin Rights)",
                            font = ("Times New Roman", 35, "bold"), background = "white", foreground = "black")
        title_label.place(x = 0, y = round(screen_height * 0.2), width = screen_width, height = 60)

        main_frame = LabelFrame(self.root, border = 2, background = "white")
        main_frame.place(x = 0, y = round(screen_height * 0.2) + 60, width = screen_width,
                         height = round(screen_height * 0.693))

        left_frame = LabelFrame(main_frame, border = 2, relief = RIDGE, text = "Attendance Details",
                                font = ("Times New Roman", 12, "bold"), background = "white")
        left_frame.place(x = 2, y = 2, width = round(screen_width * 0.4935), height = round(screen_height * 0.685))

        self.left_frame_top_photo_image = ImageTk.PhotoImage(top_right_image)
        left_frame_top_image_label = Label(left_frame, image = self.left_frame_top_photo_image)
        left_frame_top_image_label.place(x = 2, y = 2, width = round(screen_width * 0.4895),
                                         height = round(screen_height * 0.2))
        # frame inside left frame for attendance details
        left_frame_details_frame = LabelFrame(left_frame, relief = RIDGE, border = 2, background = "white")
        left_frame_details_frame.place(y = round(screen_height * 0.2) + 5, x = 2, width = round(screen_width * 0.488),
                                       height = round(screen_height * 0.45))

        # labels and entry's
        # attendance' roll_no name department time date attendance
        roll_no_label = Label(left_frame_details_frame, text = "Roll: ", background = "white",
                              font = ("Times New Roman", 15, "bold"))
        roll_no_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        roll_no_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_roll_no,
                                  font = ("Times New Roman", 15, "bold"))
        roll_no_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

        name_label = Label(left_frame_details_frame, text = "Name : ", background = "white",
                           font = ("Times New Roman", 15, "bold"))
        name_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
        name_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_name,
                               font = ("Times New Roman", 15, "bold"))
        name_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

        department_label = Label(left_frame_details_frame, text = "Department : ", background = "white",
                                 font = ("Times New Roman", 15, "bold"))
        department_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
        department_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_department,
                                     font = ("Times New Roman", 15, "bold"))
        department_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

        course_label = Label(left_frame_details_frame, text = "Course : ", background = "white",
                             font = ("Times New Roman", 15, "bold"))
        course_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)
        course_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_course,
                                 font = ("Times New Roman", 15, "bold"))
        course_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        date_label = Label(left_frame_details_frame, text = "Date : ", background = "white",
                           font = ("Times New Roman", 15, "bold"))
        date_label.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = W)
        date_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_date,
                               font = ("Times New Roman", 15, "bold"))
        date_entry.grid(row = 0, column = 4, padx = 10, pady = 5, sticky = W)

        time_label = Label(left_frame_details_frame, text = "Time : ", background = "white",
                           font = ("Times New Roman", 15, "bold"))
        time_label.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)
        time_entry = ttk.Entry(left_frame_details_frame, width = 20, textvariable = self.var_att_time,
                               font = ("Times New Roman", 15, "bold"))
        time_entry.grid(row = 1, column = 4, padx = 10, pady = 5, sticky = W)

        attendance_status_label = Label(left_frame_details_frame, text = "Status : ", background = "white",
                                        font = ("Times New Roman", 15, "bold"))
        attendance_status_label.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)
        self.var_status = ttk.Combobox(left_frame_details_frame, width = 20, textvariable = self.var_att_status,
                                       font = ("Times New Roman", 15, "bold"), state = "readonly")
        self.var_status["values"] = ("Attendance Status:", "Present", "Absent")
        self.var_status.grid(row = 2, column = 4, pady = 8)
        self.var_status.current(0)

        # buttons frame
        buttons_frame = LabelFrame(left_frame_details_frame, border = 2, relief = RIDGE, background = "white")
        buttons_frame.place(x = 2, y = round(screen_height * 0.2), width = round(screen_width * 0.483),
                            height = round(screen_height * 0.05))

        import_button = Button(buttons_frame, text = "Import csv", command = self.import_csv,
                               font = ("Times New Roman", 15, "bold"), background = "Teal", foreground = "White")
        import_button.place(x = 0, y = 0, width = round(screen_width * 0.16))

        update_button = Button(buttons_frame, text = "Update csv", command = self.update_csv,
                               font = ("Times New Roman", 15, "bold"), background = "Teal", foreground = "White")
        update_button.place(x = round(screen_width * 0.16), y = 0, width = round(screen_width * 0.16))

        reset_button = Button(buttons_frame, text = "Reset", command = self.reset_fields,
                              font = ("Times New Roman", 15, "bold"), background = "Teal", foreground = "White")
        reset_button.place(x = 2 * round(screen_width * 0.16), y = 0, width = round(screen_width * 0.16))

        # right frame
        right_frame = LabelFrame(main_frame, border = 2, relief = RIDGE, text = "Attendance Details",
                                 font = ("Times New Roman", 12, "bold"), background = "white")
        right_frame.place(x = round(screen_width * 0.5), y = 2, width = round(screen_width * 0.493),
                          height = round(screen_height * 0.685))
        table_frame = LabelFrame(right_frame, border = 2, relief = RIDGE, background = "white")
        table_frame.place(x = 2, y = 2, width = round(screen_width * 0.4895), height = round(screen_height * 0.655))

        # scroll bar table
        x_scroll = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        y_scroll = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.var_att_report_table = ttk.Treeview(table_frame, column = (
            "roll_no", "name", "department", "course", "date", "time", "attendance"), xscrollcommand = x_scroll.set,
                                                 yscrollcommand = y_scroll.set)
        x_scroll.config(command = self.var_att_report_table.xview)
        y_scroll.config(command = self.var_att_report_table.yview)

        self.var_att_report_table.heading("roll_no", text = "Roll_No")
        self.var_att_report_table.heading("name", text = "Name")
        self.var_att_report_table.heading("department", text = "Department")
        self.var_att_report_table.heading("course", text = "Course")
        self.var_att_report_table.heading("date", text = "Date")
        self.var_att_report_table.heading("time", text = "Time")
        self.var_att_report_table.heading("attendance", text = "Attendance")

        self.var_att_report_table["show"] = "headings"

        self.var_att_report_table.column("roll_no", width = round(screen_width * 0.015))
        self.var_att_report_table.column("name", width = round(screen_width * 0.04))
        self.var_att_report_table.column("department", width = round(screen_width * 0.05))
        self.var_att_report_table.column("course", width = round(screen_width * 0.05))
        self.var_att_report_table.column("date", width = round(screen_width * 0.05))
        self.var_att_report_table.column("time", width = round(screen_width * 0.05))
        self.var_att_report_table.column("attendance", width = round(screen_width * 0.05))

        self.var_att_report_table.pack(fill = BOTH, expand = 1)
        self.var_att_report_table.bind("<ButtonRelease>", self.get_cursor)

    def get_cursor(self, event=""):
        row_cursor = self.var_att_report_table.focus()
        content = self.var_att_report_table.item(row_cursor)
        rows = content["values"]
        self.var_att_roll_no.set(rows[0])
        self.var_att_name.set(rows[1])
        self.var_att_department.set(rows[2])
        self.var_att_course.set(rows[3])
        self.var_att_date.set(rows[4])
        self.var_att_time.set(rows[5])
        self.var_att_status.set(rows[6])

    def fetch_data(self, rows):
        self.var_att_report_table.delete(*self.var_att_report_table.get_children())
        for iterator in rows:
            self.var_att_report_table.insert("", END, values = iterator)

    # noinspection PyGlobalUndefined
    def import_csv(self):
        global my_data_rows
        my_data_rows.clear()
        file_to_be_imported = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV",
                                                         filetypes = (("CSV File", "*.csv"), ("All Files", ".*")),
                                                         parent = self.root)
        with open(file_to_be_imported) as operational_file:
            csv_read = csv.reader(operational_file, delimiter = ",")
            for iterator in csv_read:
                my_data_rows.append(iterator)
            self.fetch_data(my_data_rows)
        operational_file.close()

    # noinspection PyTypeChecker
    def update_csv(self):
        roll_no = self.var_att_roll_no.get()
        name = self.var_att_name.get()
        department = self.var_att_department.get()
        course = self.var_att_course.get()
        date = self.var_att_date.get()
        time = self.var_att_time.get()
        attendance = self.var_att_status.get()

        # write to csv file
        try:
            temp_operational_file = NamedTemporaryFile(mode = 'w', delete = False)
            file_to_be_updated = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (
                ("CSV File", "*.csv"), ("All File", ".*")), parent = self.root)
            with open(file_to_be_updated, mode = 'r')as operational_file, temp_operational_file:
                dict_reader = csv.DictReader(operational_file, fieldnames = (
                    ["Roll_No", "Name", "Department", "Course", "Date", "Time", "Attendance"]))  # input
                dict_writer = csv.DictWriter(temp_operational_file, lineterminator = "\n", fieldnames = (
                    ["Roll_No", "Name", "Department", "Course", "Date", "Time", "Attendance"]))  # output
                for row in dict_reader:
                    if row['Roll_No'] == roll_no:
                        if row['Date'] == str(date):
                            dict_writer.writerow({"Roll_No": roll_no, "Name": name, "Department": department,
                                                  "Course": course, "Date": date, "Time": time,
                                                  "Attendance": attendance})
                        else:
                            dict_writer.writerow({"Roll_No": row['Roll_No'], "Name": row['Name'],
                                                  "Department": row['Department'], "Course": row['Course'],
                                                  "Date": row['Date'], "Time": row['Time'],
                                                  "Attendance": row['Attendance']})

                    else:  # get data from operational file and write it to the temp_operational file
                        dict_writer.writerow({"Roll_No": row['Roll_No'], "Name": row['Name'],
                                              "Department": row['Department'], "Course": row['Course'],
                                              "Date": row['Date'], "Time": row['Time'],
                                              "Attendance": row['Attendance']})
            shutil.move(temp_operational_file.name, file_to_be_updated)
            messagebox.showinfo("Data Updated", "Your data has been updated in the " + os.path.basename(
                file_to_be_updated) + " successfully !", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Due to : {str(e)}", parent = self.root)

    def reset_fields(self):
        self.var_att_roll_no.set("")
        self.var_att_name.set("")
        self.var_att_department.set("")
        self.var_att_course.set("")
        self.var_att_date.set("")
        self.var_att_time.set("")
        self.var_att_status.set("")


if __name__ == '__main__':
    winTk = Tk()
    flag = True
    obj = AttendanceManager(winTk)

    def on_closing():
        close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
        if close:
            winTk.destroy()

    if flag:
        winTk.protocol("WM_DELETE_WINDOW", on_closing)
    winTk.mainloop()
