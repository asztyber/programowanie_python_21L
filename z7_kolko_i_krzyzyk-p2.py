#!/usr/bin/env python
# coding: utf-8

# # Kółko i krzyżyk
# 
# * Podsumowanie ifów, pętli, list i funkcji
# * my (użytkownik) gramy kółkiem (znak 'o'), a komputer krzyżykiem znak 'x'

# Plansza będzie listą trzech list

# In[71]:


plansza = [['o', 'x', 'o'], ['x', 'x', 'o'], ['o', ' ', 'x']]


# ### Zadanie 1
# Napisać **funkcję** drukującą planszą mniej więcej jak poniżej

# In[21]:


def drukuj_plansze(plansza):
    for i in range(len(plansza)):
        for a in range(len(plansza[i])):
            print(plansza[i][a], end="")
            if a < len(plansza[i])-1:
                print(" | ", end="")
        if i < len(plansza)-1:
              print("\n----------")


# In[22]:


drukuj_plansze(plansza)


# ### Zadanie 2
# Napisać **funkcję** sprawdzającą, czy któryś wiersz zawiera wyłącznie x lub o

# In[37]:


# znak to 'o' lub 'x'
def sprawdz_wiersze(plansza, znak):
    for i in range(3):
        if (plansza[i][0] == znak) and (plansza[i][1] == znak) and (plansza[i][2] == znak):
            return True
        
    return False


# In[47]:


print(sprawdz_wiersze(plansza, 'x'))


# ### Zadanie 3
# Napisać **funkcję** sprawdzającą, czy któraś **kolumna** zawiera wyłącznie x lub o

# In[48]:


def sprawdz_kolumny(plansza, znak):
    for i in range(3):
        if (plansza[0][i] == znak) and (plansza[1][i] == znak) and (plansza[2][i] == znak):
            return True
        
    return False


# In[55]:


sprawdz_kolumny(plansza, 'o')


# ### Zadanie 4
# Napisać **funkcję** sprawdzającą, czy któraś **przekątna** zawiera wyłącznie x lub o

# In[56]:


def sprawdz_przekatne(plansza, znak):
    if plansza[0][0] == znak and plansza[1][1] == znak and plansza[2][2] == znak:
        return True
    if plansza[0][2] == znak and plansza[1][1] == znak and plansza[2][0] == znak:
        return True
    
    return False


# In[66]:


sprawdz_przekatne(plansza, 'x')


# ### Zadanie 5
# Napisać **funkcję** sprawdzającą, czy któryś gracz wygrał

# In[67]:


def sprawdz_wygrana(plansza, znak):
    return (sprawdz_wiersze(plansza, znak) or sprawdz_kolumny(plansza, znak) or sprawdz_przekatne(plansza, znak))


# In[74]:


sprawdz_wygrana(plansza, 'x')


# ### Zadanie 6
# Napisać **funkcję**, która wykonuje losowy (ale poprawny ruch) x

# In[ ]:





# ### Zadanie 7
# Napisać **funkcję**, która wczytuje ruch gracza (dwie liczby) i wstawia o w odpowiednie miejsce. Wczytywanie zapętlić na wypadek nieprawidłowych danych

# In[ ]:





# ### Zadanie 8
# Napisać grę z komputerem z wykorzystaniem powyższych funkcji

# In[ ]:




