import sqlite3


class DataBase(object):
    def __init__(self, db_name: str):
        self.Connection = sqlite3.connect(db_name + ".db")
        self.Cursor = self.Connection.cursor()

    def select(self, column_name, table_name, question=None, target_value=None):
        if question:
            return self.Cursor.execute("SELECT {} FROM {} WHERE {}=?".format(column_name, table_name, question),
                                       (target_value, ))
        else:
            return self.Cursor.execute("SELECT {} FROM {}".format(column_name, table_name))

    # def insert(self, table_name, column_names, values):
    #     column_count = len(column_names)
    #     insert_str = "INSERT INTO {} ".format(table_name)
    #     names_str = "(" + ("{}, " * (column_count - 1)).format(*column_names[:-1]) + "{}".format(column_names[-1]) + ")"
    #     values_str = " VALUES(" + ("?, " * (column_count - 1)) + "?" + ")"
    #     command_str = insert_str + names_str + values_str
    #     self.Cursor.execute(command_str, values)
    #     self.Connection.commit()
    #
    # def update(self, table_name, column_names, variants, questions, target_values):
    #     column_count = len(column_names)
    #     question_count = len(questions)
    #     update_str = "UPDATE {} ".format(table_name)
    #     set_str = "SET " + ("{0}={1} AND " * (column_count - 1)).format(*column_names[:-1], *variants[:-1]) +\
    #               "{0}={1} ".format(column_names[-1], variants[-1])
    #     where_str = "WHERE " + ("{}=? AND " * (question_count - 1)).format(*questions[:-1]) +\
    #                 "{}=? ".format(questions[-1])
    #     command_str = update_str + set_str + where_str
    #     self.Cursor.execute(command_str, target_values)
    #     self.Connection.commit()
    #
    # def delete(self, table_name, questions, target_values):
    #     question_count = len(questions)
    #     delete_str = "DELETE FROM {} ".format(table_name)
    #     where_str = "WHERE " + ("{}=? AND " * (question_count - 1)).format(*questions[:-1]) + \
    #                 "{}=? ".format(questions[-1])
    #     command_str = delete_str + where_str
    #     self.Cursor.execute(command_str, target_values)
    #     self.Connection.commit()