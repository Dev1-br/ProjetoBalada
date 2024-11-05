#Entrada da balada e abordagem
import sys
print ("Bem vindo a Balada Night Blue, esperamos que sua noite seja ótima!")
idade = int(input("Qual a sua idade: "))
if idade >= 18:
    print ("Pode entrar na nossa balada.")
else:
    print ("Você não tem idade para entrar na nossa balada. Tenha uma boa noite!")
    sys.exit ()

#lista dos produtos que a balada tem para oferecer além do camarote

bebidas = ["Vodka com energético - R$ 20,00", "Whisky com energético - R$ 30,00", "Whisky Garrafa - R$ 130,00", "Água - R$ 10", "Refrigerante - R$ 15,00", "Energético - R$ 25,00", 
"Combo de Whisky - R$ 180,00", "Combo de Vodka - R$ 150,00", "Cerveja Heineken - R$ 25,00", "Cerveja Budweiser R$ 20,00"]

# Serviço de pedido do cliente

produtos = str(input("Temos no nosso cardápio de bebidas e também se desejar o nosso camarote com bebidas a vontade até ás 03:00 horas.\nO que o senhor prefere?: "))
if produtos.lower() in ["bebidas", "cardapio", "cardápio", "cardápio de bebidas", "cardápio de bebidas", "bebida", "cardapio de bebida", "cardápio de bebida"]:
    print("Aqui estão as nossas bebidas:")
    for bebida in bebidas:
        print (f"- {bebida}")
    produto = str(input("O que o senhor deseja? "))
    print ("Aguarde em uma das nossas mesas que logo traremos seu pedido.")
    sys.exit()

elif produtos.lower () == "camarote":
    print ("Nosso Camarote está custando o valor de R$ 150,00")
    produtos = str (input("Deseja adiquirir o serviço? "))

if produtos.lower () == "sim":
    print ("Me acompanhe até o nosso camarote VIP, tenho ceteza que sua experiência será incrivel!")
    sys.exit ()
elif produtos.lower () == "não" or "nao":
    print ("Então fique a vontade para curtir a pista e escolher a sua melhor bebida!")
    produtos = str (input("Deseja uma bebida agora? "))
if produtos == "não" or "nao":
    print ("Certo, qualquer pedido que queira fazer, só nos chamar.")   
    # sys.exit()

# Verificar se o cliente deseja um bebida

if produtos == "sim":
    for bebida in bebidas:
        print (f"- {bebida}")
    produtos = str (input("Qual bebida o senhor deseja? ")).strip ()
if (
    produtos.lower () == "agua" or 
    produtos.lower () == "Água" or 
    produtos.lower () == "Energetico" or
    produtos.lower () == "Energético" or 
    produtos.lower () == "Vodka com energético" or 
    produtos.lower () == "Vodka com energetico" or 
    produtos.lower () == "Whisky com energético" or 
    produtos.lower () == "Whisky com energetico" or 
    produtos.lower () == "Whisky garrafa" or
    produtos.lower () == "refrigerante" or
    produtos.lower () == "combo de whisky" or
    produtos.lower () == "combo de vodka" or
    produtos.lower () == "cerveja heineken" or
    produtos.lower () == "cerveja budweiser"
):
    print ("Aguarde em uma das nossas mesas que logo traremos seu pedido.")


        
      

         




