### curses ###

curses_data={
'curses_0':{'Clinging':0.75,'Aging':0.4, 'Hirsuitism':0.85, 'Baldness':0.8, 'Elusiveness':0.7, 'Stench':0.8, 'Swarming Insects':0.6, 'Loudness':0.8},
'curses_1':{'Weight':0.5,'the Duck-Screw':0.65, 'Polymorphing':0.85, 'Birds':0.4, 'Expansion':0.2, 'Dwarfism':0.9, 'Gigantism':0.9,},
'curses_2':{'Mania':0.5, 'Depression':0.45, 'Awkwardness':0.6, 'Weakness':0.6, 'Sickliness':0.6, 'Clumsiness':0.6, 'Obliviousness': 0.6, 'Ignorance':0.6,' the Vampire':0.2},
'curses_3':{'the Murderous Hand':-0.3, 'Water-Breathing':-0.3},
'curses_4':{'Disintegration':-1,'Transmogrification':-0.5,'Petrification':-0.7},
'non_cursed':{}
}

curses_data['curses_1'].update(curses_data['curses_0'])
curses_data['curses_2'].update(curses_data['curses_1'])
curses_data['curses_3'].update(curses_data['curses_2'])
curses_data['curses_4'].update(curses_data['curses_3'])

### currency ###
coin_value={
'Gold':1,
'Platinum':10,
'Silver':0.1,
'Copper':0.01,
'Electrum':0.5}

### gemstones ###

gems_data={
'A': ['Small Gem', 'Semi-Precious', 25],
'B': ['Medium Gem', 'Semi-Precious', 100],
'C': ['Large Gem', 'Semi-Precious', 675],
'D': ['Huge Gem', 'Semi-Precious', 6500],
'E': ['Massive Gem', 'Semi-Precious', 75000],
'F': ['Small Gem', 'Precious', 500],
'G': ['Medium Gem', 'Precious', 2000],
'H': ['Large Gem', 'Precious', 13500],
'I': ['Huge Gem', 'Precious', 125000],
'J': ['Massive Gem', 'Precious', 1500000],
'K': ['Small Gem', 'Exotic', 1500],
'L': ['Medium Gem', 'Exotic', 6000],
'M': ['Large Gem', 'Exotic', 45000],
'N': ['Huge Gem', 'Exotic', 385000],
'O': ['Massive Gem', 'Exotic', 4500000],
'P': ['Small Gem', 'Magical', 6500],
'Q': ['Medium Gem', 'Magical', 25000],
'R': ['Large Gem', 'Magical', 175000],
'S': ['Huge Gem', 'Magical', 1650000],
'T': ['Massive Gem', 'Magical', 20000000]}

gem_types={
'Semi-Precious':['Topaz','Aquamarine','Quartz','Amethyst','Opal','Fluorite','Rose Quartz','Jasper','Pearl','Amber','Agate','Chalcedony','Citrine','Beryl','Tiger-Eye','Hematite','Lapis Lazuli','Rhodonite','Snowflake Obsidian','Flame Obsidian','Tiger Obsidian','Zebra Marble'],
'Precious':['Ruby','Emerald','Sapphire','Diamond','Garnet','Blue Diamond','Yellow Diamond','Pink Diamond','Clear Sapphire','Pink Sapphire','Star Sapphire'],
'Exotic':['Mithril Sapphire','Orichalcon','Selunite','Vantacite','Dragonite','Luminous Diamond','Adamancite','Hyperpink','Limbocite','Celestite','Starfall Gem','Abyssal Shard','Inferno Pearl'],
'Magical':['Ragestone','Grimstone','Bloodstone','Gods\' Tear','Feystone','Wildstone','Chaos Stone','Law Stone','Balance Stone','Sonicstone','Thoughtstone','Voltstone','Soulstone','Moonstone','Sunstone','Dreamstone','Noostone','Shadowstone','Firestone','Earthstone','Waterstone','Windstone','Green Dragonstone','Red Dragonstone','Blue Dragonstone','White Dragonstone','Black Dragonstone','Brass Dragonstone','Bronze Dragonstone','Gold Dragonstone','Silver Dragonstone','Copper Dragonstone','Platinum Dragonstone','Polychromatic Dragonstone','Fairy Dragonstone']
}


### items ###

items_data={
'A': ['Art Piece','Typical',{'Copper {jewelry}':5,'Silver {jewelry}':35,'{instrument}':35, 'Novelty {carving} Toy':5,'Wood {carving} Carving':5,'Bone {carving} Carving':15,'Stone {carving} Carving':25,'{art} Painting':10,'{art} Sketch':10}], 
'B': ['Art Piece','Fine',{'Electrum {jewelry}':75,'Gold {jewelry}':150,'Platinum {jewelry}':350,'Finely-Crafted {instrument}':500,'{wood_0} {carving} Carving':150,'{stone_0} {carving} Carving':350,'Tasteful {art} Canvas':250,'Beautiful {art} Painting':150,'{art} Pen & Ink':75}], 
'C': ['Art Piece','Exemplary',{'Masterwork {instrument}':2000,'Impressive {art} Canvas':1000,'Memorable {art} Painting':750}], 
'D': ['Art Piece','Famed',{"~Renowned Painting: 'Psst Hey, Wanna Buy Some Cubes?":65000}], 
'E': ['Art Piece','Renowned',{"~Renowned Painting: 'Twinkling Stars'":150000,"~Renowned Sculpture: 'Fat Nuts'":690000}], 
'F': ['Weapon','Mundane',{'Shortsword':5,'Scimitar':25,'Longsword':100}], 
'G': ['Weapon','Common',{'Moon-Touched {weapon}':750}], 
'H': ['Weapon','Uncommon',{'+1 {slash}':1500,'+1 {blunt}':1500,'+1 {pierce}':1500, '+1 {thrown}':1500,'+1 {ranged}':1500,'+1 {weapon}':1500,'{element_1} {weapon}':2500,'Hewing Axe':2000, 'Lightbringer\'s Mace':2000, 'Seeker Dart':200, 'Shatterspike':2000, 'Skyblinder Staff':2500,'Staff of the Adder':2500,'Staff of the Python':2500,'Storm Boomerang':1500,'{slash} of Vengeance *':750,'Trident of Fish Command':1500,'{weapon} of Warning':1500}], 
'I': ['Weapon','Rare',{'+2 {weapon}':6500,'{element_2} {weapon}':10000,'{monster}-Slaying {weapon}':15000,'Javelin of Lightning':12000,'Dagger of Venom':12000}], 
'J': ['Weapon','Very Rare',{'+3 {weapon}':35000,'{element_3} {weapon}':50000,'Flametongue {slash}':85000, 'Greater {monster}-Slaying {weapon}':100000}], 
'K': ['Weapon','Legendary',{"~'Excalibur'":2500000,"~'Dáinslef'":1350000,"~'Joyeuse'":1690000,"~'Gungnir'":2000000,"~'Mjolnir'":2000000,"~'Gae Bolg'":1500000,"~'Ankusha'":1250000,'{weapon} Ayudhapurusha':500000,"~'Halayudha'":1000000,"~'Pasha'":650000,"~'Imhullu'":2000000,}], 
'L': ['Armor','Mundane',{'Platemail':1500,'Studded Leather':45}], 
'M': ['Armor','Common',{'{shield} of Expression':350,'Cast-Off {armor}':1500,'Gleaming {armor}':1500,'Smoldering {armor}':1500}], 
'N': ['Armor','Uncommon',{'Sentinel {shield}':1500,'Mithral {metal_armor}':1500,'Mariner\'s {armor}':2500,'Adamantine {metal_armor}':1500,'+1 {armor}':2000,'+1 {shield}':1500,'{element_1}-Absorbing {shield}':2500}], 
'O': ['Armor','Rare',{'Mind-Carapace {heavy_armor}':10000,'+1 Adamantine {metal_armor}':8500, '+2 {armor}':10000,'+2 {shield}':6500,'{element_2}-Absorbing {shield}':10000,'{armor} of {damage} Resistance':10000}], 
'P': ['Armor','Very Rare',{'+2 Adamantine {metal_armor}':35000,'+3 {armor}':50000,'+3 {shield}':35000, '{element_3}-Absorbing {shield}':50000, '{color} Dragon Scale-Mail':75000}], 
'Q': ['Armor','Legendary',{"~'Babr-e Bayan'":1500000,"~Wayland's Invincible Mail":1500000,"~Orvar-Oddr's Silken Mailcoat": 1000000, "~Armor of Achilles":2000000,"Green {armor}":500000,"Spiritual {armor} Kavacha":650000,"Sigurd's Golden Chaincoat":1000000}], 
'R': ['Wondrous Item','Common',{"Chest of Preserving":1500,"Cleansing Stone":1000,'Band of Loyalty':200,'Staff of Adornment':150,'Staff of Birdcalls':250,'Staff of Flowers':250,'Wand of Conducting':250,'Wand of Pyrotechnics':450,'Wand of Frowns':250,'Wand of Smiles':250,'Driftglobe':1000,"{instrument} of Illusions":650,"{instrument} of Scribing":500,"Imbued Wood Focus: {wood_1}":500,"Boots of False Tracks":350,"Breathing Bubble":500,"Candle of the Deep":200,"Charlatan\'s Die":200,"Cloak of Billowing":250,"Cloak of Many Fashions":350,"Clockwork Amulet":850,"Clothes of Mending":100,"Coin of Delving":50,"Dark Shard Amulet":850,"Dread Helm":650,"Ear Horn of Hearing":100,"Enduring Spellbook":650,"Ersatz Eye":500,"Everbright Lantern":750,"Featherfall Token":200,"Hat of Vermin":650,"Hat of Wizardry":850,"Heward\'s Handy Spice Pouch":750,"Horn of Silent Alarm":450,"Keycharm":500,"Lock of Trickery":350,"Mystery Key":100,"Orb of Direction":150,"Orb of Gonging":200,"Orb of Shielding: {stone_1}":850,"Orb of Time":150,"Pipe of Remembrance":650,"Pipe of Smoke Monsters":450,"Pole of Angling":100,"Pole of Collapsing":200,"Clockwork Rod & Reel":750,"Prosthetic Limb":1250,"Rope of Mending":150,"Scribe\'s Pen":450,"Sekolahian Shark Statuette":300,"Shiftweave":350,"Spellshard":400,'{jewelry} of {spell_1}':1350}], 
'S': ['Wondrous Item','Uncommon',{'Broom of Flying':4500, "Cartographer\'s Map Case":2000,'Pot of Awakening':3000, 'Bag of Holding':2500,'Gauntlets of Ogre Power':5000, 'Immovable Rod':3500, 'Cape of the Mountebank':5000,'{jewelry} of {spell_0}':3500,'{jewelry} of {spell_2}':3500,'{jewelry} of {spell_3}':6000,'{instrument} of {spell_2}':4500,'{instrument} of {spell_3}':7000}],
'T': ['Wondrous Item','Rare',{'Carpet of Flying':12500,'Dancing {weapon}':15000,'Boots of Speed':27500, 'Censer of Commanding Air Elementals':35000, 'Brazier of Commanding Fire Elementals':35000, 'Font of Commanding Water Elementals':35000, 'Stone of Commanding Earth Elementals':35000,'Boots of Levitation':8500,'Belt of Hill Giant Strength':15000,'Chime of Opening':10000,'Belt of Dwarvenkind':8500,'Cloak of the Manta-Ray':8500,'Robe of Eyes':17500,'{jewelry} of {spell_4}':15000,'{jewelry} of {spell_5}':25000,'{instrument} of {spell_4}':20000,'{instrument} of {spell_5}':30000}], 
'U': ['Wondrous Item','Very Rare',{'Cloak of Displacement':65000, 'Belt of Fire Giant Strength':150000,'Belt of Stone Giant Strength':75000, 'Belt of Ice Giant Strength':75000,'{jewelry} of {spell_6}':50000,'{jewelry} of {spell_7}':150000,'{instrument} of {spell_6}':65000,'{instrument} of {spell_7}':200000}], 
'V': ['Wondrous Item','Legendary',{'Canvass of Unchanging Self':1500000,'Belt of Cloud Giant Strength':750000, 'Belt of Storm Giant Strength':1500000,'Cubic Gate':1500000,'{jewelry} of {spell_8}':450000,'{instrument} of {spell_8}':500000,'{jewelry} of {spell_9}':1250000,'{instrument} of {spell_9}':1500000}], 
'W': ['Scroll','Cantrip',{'Scroll of {spell_0}':35}], 
'X': ['Scroll','Low-Level',{'Scroll of {spell_1}':100,'Scroll of {spell_2}':250}], 
'Y': ['Scroll','Mid-Level',{'Scroll of {spell_3}':500,'Scroll of {spell_4}':1500,'Scroll of {spell_5}':2500}], 
'Z': ['Scroll','High-Level',{'Scroll of {spell_6}':5000,'Scroll of {spell_7}':15000}],
'1': ['Scroll','Legendary',{'Scroll of {spell_8}':45000,'Scroll of {spell_9}':125000,'Scroll of Wish':500000}],
'2': ['Potion','Common',{'Potion of Watchful Rest':150,'Potion of Ogre Strength':250,'Potion of Climbing':150,'Basic Healing Potion':50,'Basic Antidote':100,'Bead of Refreshment':2,'Bead of Nourishment':2,"Moodmark Paint":135}],
'3': ['Potion','Uncommon',{'Potion of Water Breathing':350,'Potion of {damage} Resistance':500,'Potion of Shrinking':450,'Potion of Growth':450,'Potion of Hill Giant Strength':650,'Potion of Fire-Breathing':650,'Potion of Comprehension':500,'Potion of Animal Friendship':250,'Oil of Slipperiness':850,'Bottled Breath':350,"Philter of Love":500,"Perfume of Bewitching":300}],
'4': ['Potion','Rare',{"Thessaltoxin Antidote":3500,"Depth-Diving Capsule":1250,'Potion of Poison':500,'Potion of Frost Giant Strength':2000,'Potion of Stone Giant Strength':2000,'Potion of {color} Dragon\'s Breath':1750,'Lycanthropy Antidote':3500,'Mummy-Rot Antidote':3500,}],
'5': ['Potion','Very Rare',{'Potion of Fire Giant Strength':6500,'Potion of Cloud Giant Strength':10000,'Panacea':15000,'Mead of Poetry':35000,'Flask of Soma':35000,'Ampule of Ambrosia':35000}],
'6': ['Potion','Legendary',{'Potion of Storm Giant Strength':35000,'Elixir of Life':1000000,'Water of Youth':200000,'Anti-Magic Moly Tonic':25000,'Fruit of Knowledge':150000,'Fruit of Awareness':150000,'Fruit of Beauty & Wit':150000,'Fruit of Power':150000, 'Fruit of Resilience':150000,'Fruit of Finesse':150000,'Amrita':2500000}]
}

items_replace = {
'stone_0':['marble','granite','limestone','sandstone','glass'],
'stone_1':["Fernian basalt","Irian quartz","Kythrian skarn","Lamannian flint","Mabaran obsidian","Xorian marble","Risian shale","Shavaran chert"],
'wood_0':["ash","rosewood","oak","birch","cherrywood","cedar","pine","beechwood"],
'wood_1':["Fernian ash","Irian rosewood","Kythrian manchineel","Lamannian oak","Mabaran ebony","Risian pine","Shavarran birch", "Quori beech", "Xorian wenge"],
'color':['white','black','blue','red','green','black','copper','silver','gold','bronze','brass'],
'monster':['man','dragon','giant','fiend','angel','fairy'],
'slash':['handaxe','battleaxe','longsword','shortsword','saber','scimitar','greatsword','greataxe'],
'blunt':['club','mace','maul'],
'pierce':['rapier','spear','dagger','pike','lance'],
'thrown':['handaxe','dagger','boomerang','javelin','spear'],
'ranged':['shortbow','longbow','hand crossbow','light crossbow','heavy crossbow','pistol','rifle'],
'light_armor':['padded armor','leather armor','studded leather armor'],
'medium_armor':['chain shirt', 'hide armor', 'scale mail', 'breastplate', 'half-plate armor'],
'heavy_armor':['ringmail armor', 'chainmail armor', 'splint armor', 'platemail'],
'shield':['shield','kite shield','buckler','targe'],
'carving':['strange','sheep','horse','dog','cat','nude','bust','dragon','unicorn','face','phallic','angel','devil'],
'jewelry':['ring', 'necklace','bracelet','choker','broach','bangle','pin','hairpin','earring','earrings','beltbuckle','anklet','circlet','cufflinks'],
'instrument':['drum','flute','lute','lyre','horn','guitar','violin','viola','shamisen','panpipes','castinets','triangle','tuning fork','didgeridoo','ocarina'],
'art':['sunrise','sunset','landscape','battle','city','abstract','clouds', 'seascape'],
'element_1':['Heat','Spark','Chill','Sonic','Corrosive','Toxic','Bright','Withering','Psionic'],
'element_2':['Flame','Lightning','Frostbite','Shockwave','Acid','Poison','Radiant','Necrotic','Mindstrike'],
'element_3':['Blaze','Boltstrike','Deepfreeze','Shattering','Venom','Scintillating','Rotting','Fluroantimonic','Braindeath'],
'physical_damage':['piercing','slashing','bludgeoning'],
'magic_damage':['fire','cold','lightning','thunder','poison','acid','radiant','necrotic','force','psychic'],
'spell_0':["'Acid Splash'","'Blade Ward'","'Booming Blade'","'Chill Touch'","'Control Flames'","'Create Bonfire'","'Dancing Lights'","'Druidcraft'","'Eldritch Blast'","'Encode Thoughts'","'Fire Bolt'","'Friends'","'Frostbite'","'Green-Flame Blade'","'Guidance'","'Gust'","'Infestation'","'Light'","'Lightning Lure'","'Mage Hand'","'Magic Stone'","'Mending'","'Message'","'Mind Sliver'","'Minor Illusion'","'Mold Earth'","'Poison Spray'","'Prestidigitation'","'Primal Savagery'","'Produce Flame'","'Ray of Frost'","'Resistance'","'Sacred Flame'","'Sapping Sting'","'Shape Water'","'Shillelagh'","'Shocking Grasp'","'Spare the Dying'","'Sword Burst'","'Thaumaturgy'","'Thorn Whip'","'Thunderclap'","'Toll the Dead'","'True Strike'","'Vicious Mockery'","'Word of Radiance'"],
'spell_1':["'Absorb Elements'","'Acid Stream'","'Alarm'","'Burning Hands'","'Catapult'","'Cause Fear'","'Charm Person'","'Chromatic Orb'","'Color Spray'","'Comprehend Languages'","'Detect Magic'","'Disguise Self'","'Distort Value'","'Earth Tremor'","'Expeditious Retreat'","'False Life'","'Feather Fall'","'Find Familiar'","'Floating Disk'","'Fog Cloud'","'Grease'","'Hideous Laughter'","'Ice Knife'","'Identify'","'Illusory Script'","'Jump'","'Longstrider'","'Mage Armor'","'Magic Missile'","'Protection from Evil and Good'","'Ray of Sickness'","'Shield'","'Silent Image'","'Sleep'","'Snare'","'Tasha\'s Hideous Laughter'","'Tenser\'s Floating Disk'","'Thunderwave'","'Unseen Servant'","'Witch Bolt'"],
'spell_2':["'Acid Arrow'","'Aganazzar\'s Scorcher'","'Aid'","'Alter Self'","'Animal Messenger'","'Arcane Lock'","'Arcanist\'s Magic Aura'","'Augury'","'Barkskin'","'Beast Sense'","'Blindness/Deafness'","'Blur'","'Branding Smite'","'Calm Emotions'","'Cloud of Daggers'","'Continual Flame'","'Cordon of Arrows'","'Crown of Madness'","'Darkness'","'Darkvision'","'Detect Thoughts'","'Dragon\'s Breath'","'Dust Devil'","'Earthbind'","'Enhance Ability'","'Enlarge/Reduce'","'Enthrall'","'Find Steed'","'Find Traps'","'Flame Blade'","'Flaming Sphere'","'Flock of Familiars'","'Fortune\'s Favor'","'Gentle Repose'","'Gift of Gab'","'Gust of Wind'","'Healing Spirit'","'Heat Metal'","'Hold Person'","'Immovable Object'","'Invisibility'","'Jim\'s Glowing Coin'","'Knock'","'Lesser Restoration'","'Levitate'","'Locate Animals or Plants'","'Locate Object'","'Magic Mouth'","'Magic Weapon'","'Maximilian\'s Earthen Grasp'","'Melf\'s Acid Arrow'","'Mind Spike'","'Mind Thrust'","'Mirror Image'","'Misty Step'","'Moonbeam'","'Nystul\'s Magic Aura'","'Pass without Trace'","'Phantasmal Force'","'Prayer of Healing'","'Protection from Poison'","'Pyrotechnics'","'Ray of Enfeeblement'","'Rope Trick'","'Scorching Ray'","'See Invisibility'","'Shadow Blade'","'Shatter'","'Silence'","'Skywrite'","'Snilloc\'s Snowball Swarm'","'Spider Climb'","'Spike Growth'","'Spiritual Weapon'","'Suggestion'","'Summon Bestial Spirit'","'Warding Bond'","'Warding Wind'","'Web'","'Wristpocket'","'Zone of Truth'"],
'spell_3':["'Animate Dead'","'Aura of Vitality'","'Beacon of Hope'","'Bestow Curse'","'Blinding Smite'","'Blink'","'Call Lightning'","'Catnap'","'Clairvoyance'","'Conjure Animals'","'Conjure Barrage'","'Counterspell'","'Create Food and Water'","'Crusader\'s Mantle'","'Daylight'","'Dispel Magic'","'Elemental Weapon'","'Enemies Abound'","'Erupting Earth'","'Fast Friends'","'Fear'","'Feign Death'","'Fireball'","'Flame Arrows'","'Fly'","'Galder\'s Tower'","'Gaseous Form'","'Glyph of Warding'","'Haste'","'Hunger of Hadar'","'Hypnotic Pattern'","'Incite Greed'","'Leomund\'s Tiny Hut'","'Life Transference'","'Lightning Arrow'","'Lightning Bolt'","'Magic Circle'","'Major Image'","'Mass Healing Word'","'Meld into Stone'","'Melf\'s Minute Meteors'","'Motivational Speech'","'Nondetection'","'Phantom Steed'","'Plant Growth'","'Protection from Energy'","'Pulse Wave'","'Remove Curse'","'Revivify'","'Sending'","'Sleet Storm'","'Slow'","'Speak with Dead'","'Speak with Plants'","'Spirit Guardians'","'Spirit Shroud'","'Stinking Cloud'","'Summon Fey Spirit'","'Summon Lesser Demons'","'Summon Shadow Spirit'","'Summon Undead Spirit'","'Thunder Step'","'Tidal Wave'","'Tiny Hut'","'Tiny Servant'","'Tongues'","'Vampiric Touch'","'Wall of Sand'","'Wall of Water'","'Water Breathing'","'Water Walk'","'Wind Wall'"],
'spell_4':["'Arcane Eye'","'Aura of Life'","'Aura of Purity'","'Banishment'","'Black Tentacles'","'Blight'","'Charm Monster'","'Compulsion'","'Confusion'","'Conjure Minor Elementals'","'Conjure Woodland Beings'","'Control Water'","'Death Ward'","'Dimension Door'","'Divination'","'Dominate Beast'","'Elemental Bane'","'Evard\'s Black Tentacles'","'Fabricate'","'Faithful Hound'","'Find Greater Steed'","'Fire Shield'","'Freedom of Movement'","'Galder\'s Speedy Courier'","'Giant Insect'","'Grasping Vine'","'Gravity Sinkhole'","'Greater Invisibility'","'Guardian of Faith'","'Guardian of Nature'","'Hallucinatory Terrain'","'Ice Storm'","'Intellect Fortress'","'Leomund\'s Secret Chest'","'Locate Creature'","'Mordenkainen\'s Faithful Hound'","'Mordenkainen\'s Private Sanctum'","'Otiluke\'s Resilient Sphere'","'Phantasmal Killer'","'Polymorph'","'Private Sanctum'","'Resilient Sphere'","'Secret Chest'","'Shadow of Moil'","'Sickening Radiance'","'Staggering Smite'","'Stone Shape'","'Stoneskin'","'Storm Sphere'","'Summon Aberrant Spirit'","'Summon Elemental Spirit'","'Summon Greater Demon'","'Vitriolic Sphere'","'Wall of Fire'","'Watery Sphere'"],
'spell_5':["'Animate Objects'","'Antilife Shell'","'Arcane Hand'","'Awaken'","'Banishing Smite'","'Bigby\'s Hand'","'Circle of Power'","'Cloudkill'","'Commune'","'Commune with Nature'","'Cone of Cold'","'Conjure Elemental'","'Conjure Volley'","'Contact Other Plane'","'Contagion'","'Control Winds'","'Creation'","'Danse Macabre'","'Dawn'","'Destructive Wave'","'Dispel Evil and Good'","'Dominate Person'","'Dream'","'Enervation'","'Far Step'","'Flame Strike'","'Geas'","'Greater Restoration'","'Hallow'","'Hold Monster'","'Holy Weapon'","'Immolation'","'Infernal Calling'","'Insect Plague'","'Legend Lore'","'Maelstrom'","'Mass Cure Wounds'","'Mislead'","'Modify Memory'","'Negative Energy Flood'","'Passwall'","'Planar Binding'","'Raise Dead'","'Rary\'s Telepathic Bond'","'Reincarnate'","'Scrying'","'Seeming'","'Skill Empowerment'","'Steel Wind Strike'","'Summon Celestial Spirit'","'Swift Quiver'","'Synaptic Static'","'Telekinesis'","'Telepathic Bond'","'Teleportation Circle'","'Temporal Shunt'","'Transmute Rock'","'Tree Stride'","'Wall of Force'","'Wall of Light'","'Wall of Stone'","'Wrath of Nature'"],
'spell_6':["'Arcane Gate'","'Blade Barrier'","'Bones of the Earth'","'Chain Lightning'","'Circle of Death'","'Conjure Fey'","'Contingency'","'Create Homunculus'","'Create Undead'","'Disintegrate'","'Drawmij\'s Instant Summons'","'Druid\'s Grove'","'Eyebite'","'Find the Path'","'Flesh to Stone'","'Forbiddance'","'Freezing Sphere'","'Globe of Invulnerability'","'Gravity Fissure'","'Guards and Wards'","'Harm'","'Heal'","'Heroes\' Feast'","'Instant Summons'","'Investiture of Flame'","'Investiture of Ice'","'Investiture of Stone'","'Investiture of Wind'","'Magic Jar'","'Mass Suggestion'","'Mental Prison'","'Move Earth'","'Otherworldly Form'","'Otiluke\'s Freezing Sphere'","'Otto\'s Irresistible Dance'","'Planar Ally'","'Primordial Ward'","'Programmed Illusion'","'Scatter'","'Soul Cage'","'Summon Fiendish Spirit'","'Sunbeam'","'Tenser\'s Transformation'","'Transport via Plants'","'True Seeing'","'Wall of Ice'","'Wall of Thorns'","'Wind Walk'","'Word of Recall'"],
'spell_7':["'Conjure Celestial'","'Crown of Stars'","'Delayed Blast Fireball'","'Divine Word'","'Etherealness'","'Finger of Death'","'Fire Storm'","'Forcecage'","'Magnificent Mansion'","'Mirage Arcane'","'Mordenkainen\'s Magnificent Mansion'","'Mordenkainen\'s Sword'","'Plane Shift'","'Power Word Pain'","'Prismatic Spray'","'Project Image'","'Regenerate'","'Resurrection'","'Reverse Gravity'","'Sequester'","'Simulacrum'","'Symbol'","'Teleport'","'Temple of the Gods'","'Tether Essence'","'Whirlwind'"],
'spell_8':["'Control Weather'","'Antimagic Field'","'Abi-Dalzim\'s Horrid Wilting'","'Dominate Monster'","'Incendiary Cloud'","'Maddening Darkness'","'Reality Break'","'Animal Shapes'","'Earthquake'","'Holy Aura'","'Dark Star'","'Illusory Dragon'","'Antipathy/Sympathy'","'Tsunami'","'Mighty Fortress'","'Maze'","'Feeblemind'","'Power Word Stun'","'Telepathy'","'Mind Blank'","'Sunburst'","'Clone'","'Glibness'","'Demiplane'"],
'spell_9':["'Mass Polymorph'","'True Polymorph'","'Storm of Vengeance'","'Invulnerability'","'Shapechange'","'Ravenous Void'","'Gate'","'Astral Projection'","'True Resurrection'","'Weird'","'Imprisonment'","'Power Word Heal'","'Prismatic Wall'","'Time Ravage'","'Power Word Kill'","'Foresight'","'Psychic Scream'","'Meteor Swarm'","'Time Stop'","'Mass Heal'"]
}

items_replace['damage'] = items_replace['physical_damage'] + items_replace['magic_damage']
items_replace['weapon'] = items_replace['slash'] + items_replace['blunt'] + items_replace['pierce'] + items_replace['ranged'] + items_replace['thrown']
items_replace['armor'] = items_replace['light_armor'] + items_replace['medium_armor'] + items_replace['heavy_armor']
items_replace['metal_armor'] = ['chain shirt', 'scale mail', 'breastplate', 'half-plate armor','ringmail armor', 'chainmail armor', 'splint armor', 'platemail']
items_replace['art'].extend(items_replace['carving'])
