alplabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
text = input("Enter the text\n").lower()
shift = int(input("Enter the shift number\n"))

def encrypt(original_text,shift_amount):
  cipher_text = "" 
  for i in original_text:
    shifted_position = alplabet.index(i) + shift_amount
    shifted_position = shifted_position % len(alplabet)
    cipher_text += alplabet[shifted_position]
  print(f"here is the encoded result :{cipher_text}")
encrypt(original_text=text,shift_amount=shift)




