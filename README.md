# Mission Extract

Mission_Extract — это программа для извлечения файлов из архива \[level.pak\] из игрового движка CryEngine 3, необходимых для работы программы [CryLevelConvert.exe](https://github.com/prophetl33t/CryLevelConvert), а также для её последующего запуска. Вторично извлекает папку \[brush\] и файлы \[LightSettings.lgt\] и \[VegetationObject.veg\], наконец, программа собирает всё в одну папку с названием уровня.

Папка \[brush\] - содержит cgf-файлы [Solid](https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/1048697)

Файл \[LightSettings.lgt\] - содержит значения для параметров [Terrain Lighting Tool](https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/1048741) для импортирования в Sandbox Editor

Файл \[VegetationObject.veg\] - содержит объекты растительности, которые используется на карте (только информацию, без координат каждого объекта)
