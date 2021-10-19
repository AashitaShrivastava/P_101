import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                
                with open(file_from, 'rb') as f:
                  dbx.files_upload(f.read(), dropbox_path,mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = "g_r20q2RAHEAAAAAAAAAASfSpOc3w9YiMKWynsndARuzpPIk9mcQ2hc38hqmglaJ"
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test2.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
