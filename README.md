# Mission Extract

Mission_Extract — это программа для извлечения файлов из архивов уровня игрового движка CryEngine 3, необходимых для работы программы [CryLevelConvert.exe](https://github.com/prophetl33t/CryLevelConvert) и для её последующего запуска. Вторично извлекает: папку \[brush\] и файлы \[LightSettings.lgt\] и \[VegetationObject.veg\], наконец, программа собирает всё в одну папку с названием уровня.

## Немного определений:
Папка \[brush\] - содержит cgf-файлы [Solid](https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/1048697);

Файл \[LightSettings.lgt\] - содержит значения для параметров [Terrain Lighting Tool](https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/1048741) для импортирования в Sandbox Editor;

Файл \[VegetationObject.veg\] - содержит объекты [Vegetation](https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/1310884), которые используется на карте, для дальнейшего импортирования в Sandbox Editor. Файл содержит только основную информацию об используюмых объектах, без координат и параметров каждого отдельного объекта;

## Для работы программы требуется:
- [CryLevelConvert.exe](https://github.com/prophetl33t/CryLevelConvert) последней версии и файлы необходимые для его корректной работы;
- Расшифрованные архивы уровня \[level.pak\] и \[terraintexture.pak\];

Это всё должно лежать в одной директории с программой.

## Зачем нужна данная программа?

Программа является своеобразным дополнением к [CryLevelConvert.exe](https://github.com/prophetl33t/CryLevelConvert), что позволяет упростить и ускорить работу с ним в несколько раз. Вместо того, чтобы собирать все файлы по директории, они будут ждать вас в одной папке, так ещё и будут отсортированы по назначению. Ну и также программа извлечёт те файлы, которые CryLevelConvert не извлекает.

![image](https://github.com/user-attachments/assets/816d03d1-8772-4eac-b3c1-ca3126056abc)
