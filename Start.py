impor sys

impor keyGen
impor keysend
impor mainReceiver
impor mainSender
impor requestPublicKey



 menu def ():
	sementara ( Benar ):
		choice =  raw_input ( " Tekan 1 untuk Menghasilkan Kunci baru, Tekan 2 untuk Mengirim Kunci Anda kepada seseorang, Tekan 3 untuk meminta kunci publik dari seseorang, Tekan 4 untuk Mengenkripsi Pesan, Tekan 5 untuk Mendekripsi Pesan \ r " )
		
		if (choice ==  ' 1 ' ):
			keyGen.runKeyGen ()
		if (choice ==  ' 2 ' ):
			keysend.runKeySend ()
		if (choice ==  ' 3 ' ):
			requestPublicKey.runReq ()
		if (choice ==  ' 4 ' ):
			mainSender.mainSender ()
		if (choice ==  ' 5 ' ):
			mainReceiver.mainReceiver ()
		


menu()
