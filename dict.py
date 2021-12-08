
print('menampilkan kontak ari')
daftar_kontak = {'ari':'081267888','dina': '087677776'}
print(daftar_kontak['ari'])

print('menambh kontak baru')
daftar_kontak['riko'] = '087654544'
print(daftar_kontak)

print('menganti nilai baru')
daftar_kontak['dina'] = '088999776';
print(daftar_kontak)

print('memampilkan semua nama')
print(daftar_kontak.keys())

print('memanmpilkan semua nomer')
print(daftar_kontak.values())

print('menampilkan semua daftar nomer nya ')
print(daftar_kontak.items())

print('menghapus nilai dina')
del(daftar_kontak['dina'])

print(daftar_kontak)


