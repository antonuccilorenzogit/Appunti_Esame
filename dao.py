class DAO:
    @staticmethod
    def get_geni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  """

        cursor.execute(query, (   ,))

        for row in cursor:
            result.append(Obj(row['']))

        cursor.close()
        conn.close()
        return result
