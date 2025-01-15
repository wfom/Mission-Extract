import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
import os
import subprocess
import shutil
from shutil import move

input("\n\n⚠️ Attention! During the execution of the program, you must press the [Enter] key so that it continues to work. Press the [Enter] key to start working...\n\n")

try:
    if not os.path.exists('level.pak') and not os.path.exists('terraintexture.pak'):
        raise ValueError("The [level.pak] and [terraintexture.pak] archives were not found. Check if these files are in the directory.")
    elif not os.path.exists('level.pak'):
        raise ValueError("The [level.pak] archive was not found. Check if this file is in the directory.")
    elif not os.path.exists('terraintexture.pak'):
        raise ValueError("The [terraintexture.pak] archive was not found. Check if this file is in the directory.")
    with zipfile.ZipFile('level.pak') as zf:
        for file in zf.namelist():
            if file.startswith('brush/'):
                extract_path = os.path.join(file)
                os.makedirs(os.path.dirname(extract_path), exist_ok=True)
                with open(extract_path, 'wb') as f:
                    f.write(zf.read(file))
        print('- Extracted folder: [brush]')
        zf.extract("mission_mission0.xml")
        print('- The file was extracted: [mission_mission0.xml]')
        zf.extract("leveldata.xml")
        print('- The file was extracted: [leveldata.xml]')
        zf.extract("moviedata.xml")
        print('- The file was extracted: [moviedata.xml]')
    leveldata = ET.parse('leveldata.xml').getroot()
    for tag in leveldata.findall('LevelInfo'):
        NameLevel = tag.attrib['Name']
    print(f'- Level Name:: [{NameLevel}]')
    if not os.path.isdir(NameLevel):
        Folders = [NameLevel, f"{NameLevel}/Setting", f"{NameLevel}/Setting/Layers", f"{NameLevel}/Setting/TOD_and_Lighting", f"{NameLevel}/Setting/Terrain", f"{NameLevel}/Setting/Vegetation"]
        for Folder in Folders:
            os.mkdir(Folder)
            print(f"- A new directory has been created: [{Folder}]")
    print('- Launch: [CryLevelConvert.exe]\n-------------------------------------------------------------------------------------')
    subprocess.run(['CryLevelConvert.exe'])
    for file in os.listdir():
        if file.endswith('.lyr'):
            source_file = file
            target_file = os.path.join(f"{NameLevel}\\Setting\\Layers\\", file)
            try:
                move(source_file, target_file)
            except OSError as e:
                print(f'An error occurred while moving the file!\nFile: {e.filename}')
    shutil.move("brush", f"{NameLevel}\\brush")
    move("TimeOfDay.tod", f"{NameLevel}\\Setting\\TOD_and_Lighting\\")
    move("TerrainLayerTexInfo.lay", f"{NameLevel}\\Setting\\Terrain\\")
    move("level.pak", f"{NameLevel}\\")
    move("terraintexture.pak", f"{NameLevel}\\")
    print('-------------------------------------------------------------------------------------\n- Working with the program [CryLevelConvert.exe] completed. The created files are distributed in directories.')
    os.remove('moviedata.xml')
    print('- The file was deleted: [moviedata.xml]')
    os.remove('EntityArchetypeData.clcdb')
    print('- The file was deleted: [EntityArchetypeData.clcdb]')

    mission_mission = ET.parse('mission_mission0.xml').getroot()
    for tag in mission_mission.findall('Environment/Lighting'): 
        SunRotation = tag.attrib['SunRotation']
        SunHeight = tag.attrib['SunHeight']
        Algorithm = tag.attrib['Algorithm']
        Lighting = tag.attrib['Lighting']
        Shadows = tag.attrib['Shadows']
        ShadowIntensity = tag.attrib['ShadowIntensity']
        ILQuality = tag.attrib['ILQuality']
        HemiSamplQuality = tag.attrib['HemiSamplQuality']
        Longitude = tag.attrib['Longitude']
        DawnTime = tag.attrib['DawnTime']
        DawnDuration = tag.attrib['DawnDuration']
        DuskTime = tag.attrib['DuskTime']
        DuskDuration = tag.attrib['DuskDuration']
        SunVector = tag.attrib['SunVector']
    LightSettings = f'<LightSettings>\n    <Lighting SunRotation="{SunRotation}" SunHeight="{SunHeight}" Algorithm="{Algorithm}" Lighting="{Lighting}" Shadows="{Shadows}" ShadowIntensity="{ShadowIntensity}" ILQuality="{ILQuality}" HemiSamplQuality="{HemiSamplQuality}" Longitude="{Longitude}" DawnTime="{DawnTime}" DawnDuration="{DawnDuration}" DuskTime="{DuskTime}" DuskDuration="{DuskDuration}" SunVector="{SunVector}"/>\n</LightSettings>'
    with open(f'{NameLevel}/Setting/TOD_and_Lighting/LightSettings.lgt', "w+") as f:
        f.write(LightSettings)
    print('- The file was extracted: [LightSettings.lgt]')
    os.remove('mission_mission0.xml')
    print('- The file was deleted: [mission_mission0.xml]')
    Vegetation = "<Vegetation>"
    for tag in leveldata.findall('Vegetation/Object'): 
        try:
            Size = tag.attrib['Size']
        except:
            Size = ""
        try:
            SizeVar = tag.attrib['SizeVar']
        except:
            SizeVar = ""
        try:
            RandomRotation = tag.attrib['RandomRotation']
        except:
            RandomRotation = ""
        try:
            AlignToTerrain = tag.attrib['AlignToTerrain']
        except:
            AlignToTerrain = ""
        try:
            UseTerrainColor = tag.attrib['UseTerrainColor']
        except:
            UseTerrainColor = ""
        try:
            AllowIndoor = tag.attrib['AllowIndoor']
        except:
            AllowIndoor = ""
        try:
            Bending = tag.attrib['Bending']
        except:
            Bending = ""
        try:
            Hideable = tag.attrib['Hideable']
        except:
            Hideable = ""
        try:
            PlayerHideable = tag.attrib['PlayerHideable']
        except:
            PlayerHideable = ""
        try:
            GrowOnVoxels = tag.attrib['GrowOnVoxels']
        except:
            GrowOnVoxels = ""
        try:
            GrowOnBrushes = tag.attrib['GrowOnBrushes']
        except:
            GrowOnBrushes = ""
        try:
            Pickable = tag.attrib['Pickable']
        except:
            Pickable = ""
        try:
            AIRadius = tag.attrib['AIRadius']
        except:
            AIRadius = ""
        try:
            Brightness = tag.attrib['Brightness']
        except:
            Brightness = ""
        try:
            Density = tag.attrib['Density']
        except:
            Density = ""
        try:
            ElevationMin = tag.attrib['ElevationMin']
        except:
            ElevationMin = ""
        try:
            ElevationMax = tag.attrib['ElevationMax']
        except:
            ElevationMax = ""
        try:
            SlopeMin = tag.attrib['SlopeMin']
        except:
            SlopeMin = ""
        try:
            SlopeMax = tag.attrib['SlopeMax']
        except:
            SlopeMax = ""
        try:
            CastShadow = tag.attrib['CastShadow']
        except:
            CastShadow = ""
        try:
            RecvShadow = tag.attrib['RecvShadow']
        except:
            RecvShadow = ""
        try:
            AlphaBlend = tag.attrib['AlphaBlend']
        except:
            AlphaBlend = ""
        try:
            SpriteDistRatio = tag.attrib['SpriteDistRatio']
        except:
            SpriteDistRatio = ""
        try:
            LodDistRatio = tag.attrib['LodDistRatio']
        except:
            LodDistRatio = ""
        try:
            MaxViewDistRatio = tag.attrib['MaxViewDistRatio']
        except:
            MaxViewDistRatio = ""
        try:
            Material = tag.attrib['Material']
        except:
            Material = ""
        try:
            UseSprites = tag.attrib['UseSprites']
        except:
            UseSprites = ""
        try:
            MinSpec = tag.attrib['MinSpec']
        except:
            MinSpec = ""
        try:
            MaxSpec = tag.attrib['MaxSpec']
        except:
            MaxSpec = ""
        try:
            Frozen = tag.attrib['Frozen']
        except:
            Frozen = ""
        try:
            Layer_Wet = tag.attrib['Layer_Wet']
        except:
            Layer_Wet = ""
        try:
            Object = tag.attrib['Object']
        except:
            Object = ""
        try:
            Id = tag.attrib['Id']
        except:
            Id = ""
        try:
            GUID = tag.attrib['GUID']
        except:
            GUID = ""
        try:
            Hidden = tag.attrib['Hidden']
        except:
            Hidden = ""
        try:
            Index = tag.attrib['Index']
        except:
            Index = ""
        try:
            Category = tag.attrib['Category']
        except:
            Category = ""
        Vegetation += f'\n    <VegetationObject Size="{Size}" SizeVar="{SizeVar}" RandomRotation="{RandomRotation}" AlignToTerrain="{AlignToTerrain}" UseTerrainColor="{UseTerrainColor}" AllowIndoor="{AllowIndoor}" Bending="{Bending}" Hideable="{Hideable}" PlayerHideable="{PlayerHideable}" GrowOnVoxels="{GrowOnVoxels}" GrowOnBrushes="{GrowOnBrushes}" Pickable="{Pickable}" AIRadius="{AIRadius}" Brightness="{Brightness}" Density="{Density}" ElevationMin="{ElevationMin}" ElevationMax="{ElevationMax}" SlopeMin="{SlopeMin}" SlopeMax="{SlopeMax}" CastShadow="{CastShadow}" RecvShadow="{RecvShadow}" AlphaBlend="{AlphaBlend}" SpriteDistRatio="{SpriteDistRatio}" LodDistRatio="{LodDistRatio}" MaxViewDistRatio="{MaxViewDistRatio}" Material="{Material}" UseSprites="{UseSprites}" MinSpec="{MinSpec}" MaxSpec="{MaxSpec}" Frozen="{Frozen}" Layer_Wet="{Layer_Wet}" Object="{Object}" Id="{Id}" GUID="{GUID}" Hidden="{Hidden}" Index="{Index}" Category="{Category}" />'
    Vegetation += "\n</Vegetation>"
    with open(f'{NameLevel}/Setting/Vegetation/VegetationObject.veg', "w+") as f:
        f.write(Vegetation)
    print('- The file was extracted: [VegetationObject.veg]')
    os.remove('leveldata.xml')
    print('- The file was deleted: [leveldata.xml]')
    input("\n\nThe program has been successfully completed, you can close the program by simply pressing the [Enter] key...")
except Exception as e:
    e = str(e)
    if e == "[Errno 2] No such file or directory: 'level.pak'":
        input("Error: The [level.pak] archive was not found. Check if this file is in the directory.")
    elif e == "Bad magic number for central directory":
        input("Error: The [level.pak] archive has not been decrypted. Decrypt the archive and try again.")
    else:
        input(f'Error: {e}')
