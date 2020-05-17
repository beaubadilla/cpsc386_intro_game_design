from block import Block
from item import Item
import pygame

class Placement:

    def __init__(self):
        self.brick153 = None
        self.brick157 = None

    def place_bricks(self, screen, question_block_images, overworld_brick_images, overworld_stair_image, pipe_image, blocks,
                     static_coin_images, mushroom_image, flower_images, star_images, coins, coins2,items,):
        # Initializing all necessary items
        for num_coins in range(10):
            new_coin = Item(screen, static_coin_images, 4)
            items.add(new_coin)
            coins.append(new_coin)

        #coin1 = Item(screen, static_coin_images, 4)
        #coin1.rect.center = (150, 450 + 222)
        #coins2.append(coin1)

        mushroom1 = Item(screen, mushroom_image, 1)
        # mushroom2 = Item(screen, mushroom_image, 1)
        # mushroom3 = Item(screen, mushroom_image, 1)
        flower1 = Item(screen, flower_images, 1)
        # flower2 = Item(screen, flower_images, 1)
        star1 = Item(screen, star_images, 3)
        items.add(mushroom1)
        items.add(flower1)
        items.add(star1)

        # y-values of potential '?' blocks
        y_low_level = 287
        y_high_level = 159

        block1 = Block(screen, '?', question_block_images, coins[0])
        block1.rect.center = (527, 287)
        coins[0].rect.centery = y_low_level

        block2 = Block(screen, 'ow_brick', overworld_brick_images)
        block3 = Block(screen, '?', question_block_images, mushroom1)
        block4 = Block(screen, 'ow_brick', overworld_brick_images)
        block5 = Block(screen, '?', question_block_images, coins[1])
        # coins[1].rect.centery = y_low_level
        block6 = Block(screen, 'ow_brick', overworld_brick_images)
        block2.rect.center = (658, 287)
        block3.rect.center = (665, 287)
        mushroom1.rect.centery = y_low_level
        block4.rect.center = (665, 287)
        block5.rect.center = (665, 287)
        coins[1].rect.centery = y_low_level
        block6.rect.center = (665, 287)
        block3.rect.left = block2.rect.right
        block4.rect.left = block3.rect.right
        block5.rect.left = block4.rect.right
        block6.rect.left = block5.rect.right

        block7 = Block(screen, 'ow_brick', overworld_brick_images)
        block8 = Block(screen, '?', question_block_images, star1)
        star1.rect.centery = y_low_level
        block9 = Block(screen, 'ow_brick', overworld_brick_images)
        block7.rect.center = (2478, 287)
        block8.rect.center = (2478, 287)
        block9.rect.center = (2478, 287)
        block8.rect.left = block7.rect.right
        block9.rect.left = block8.rect.right

        block10 = Block(screen, 'ow_brick', overworld_brick_images)
        block10.rect.center = (3022, 287)

        block11 = Block(screen, 'ow_brick', overworld_brick_images)
        block12 = Block(screen, 'ow_brick', overworld_brick_images)
        block11.rect.center = (3214, 287)
        block12.rect.center = (3022, 287)
        block12.rect.left = block11.rect.right

        block13 = Block(screen, '?', question_block_images, coins[3])
        block13.rect.center = (3406, 287)
        coins[3].rect.centery = y_low_level

        block14 = Block(screen, '?', question_block_images, coins[4])
        block14.rect.center = (3502, 287)
        coins[4].rect.centery = y_low_level

        block15 = Block(screen, '?', question_block_images, coins[5])
        block15.rect.center = (3598, 287)
        coins[5].rect.centery = y_low_level

        block16 = Block(screen, 'ow_brick', overworld_brick_images)
        block16.rect.center = (3790, 287)

        block17 = Block(screen, 'ow_brick', overworld_brick_images)
        block18 = Block(screen, 'ow_brick', overworld_brick_images)
        block17.rect.center = (4141, 287)
        block18.rect.center = (3022, 287)
        block18.rect.left = block17.rect.right

        block19 = Block(screen, 'ow_brick', overworld_brick_images)
        block20 = Block(screen, 'ow_brick', overworld_brick_images)
        block21 = Block(screen, '?', question_block_images, coins[6])
        coins[6].rect.centery = y_low_level
        block22 = Block(screen, 'ow_brick', overworld_brick_images)
        block19.rect.center = (5389, 287)
        block20.rect.center = (4141, 287)
        block21.rect.center = (4141, 287)
        block22.rect.center = (4141, 287)
        block20.rect.left = block19.rect.right
        block21.rect.left = block20.rect.right
        block22.rect.left = block21.rect.right

        block23 = Block(screen, '?', question_block_images, coins[7])
        block23.rect.center = (717, 159)
        coins[7].rect.centery = y_high_level

        block24 = Block(screen, 'ow_brick', overworld_brick_images)
        block25 = Block(screen, 'ow_brick', overworld_brick_images)
        block26 = Block(screen, 'ow_brick', overworld_brick_images)
        block27 = Block(screen, 'ow_brick', overworld_brick_images)
        block28 = Block(screen, 'ow_brick', overworld_brick_images)
        block29 = Block(screen, 'ow_brick', overworld_brick_images)
        block30 = Block(screen, 'ow_brick', overworld_brick_images)
        block31 = Block(screen, 'ow_brick', overworld_brick_images)
        block24.rect.center = (2574, 159)
        block25.rect.center = (717, 159)
        block26.rect.center = (717, 159)
        block27.rect.center = (717, 159)
        block28.rect.center = (717, 159)
        block29.rect.center = (717, 159)
        block30.rect.center = (717, 159)
        block31.rect.center = (717, 159)
        block25.rect.left = block24.rect.right
        block26.rect.left = block25.rect.right
        block27.rect.left = block26.rect.right
        block28.rect.left = block27.rect.right
        block29.rect.left = block28.rect.right
        block30.rect.left = block29.rect.right
        block31.rect.left = block30.rect.right

        block32 = Block(screen, 'ow_brick', overworld_brick_images)
        block33 = Block(screen, 'ow_brick', overworld_brick_images)
        block34 = Block(screen, 'ow_brick', overworld_brick_images)
        block35 = Block(screen, '?', question_block_images, coins[2])
        coins[2].rect.centery = y_high_level
        block32.rect.center = (2925, 159)
        block33.rect.center = (717, 159)
        block34.rect.center = (717, 159)
        block35.rect.center = (717, 159)
        block33.rect.left = block32.rect.right
        block34.rect.left = block33.rect.right
        block35.rect.left = block34.rect.right

        block36 = Block(screen, '?', question_block_images, flower1)
        block36.rect.center = (3504, 159)
        flower1.rect.centery = y_high_level

        block37 = Block(screen, 'ow_brick', overworld_brick_images)
        block38 = Block(screen, 'ow_brick', overworld_brick_images)
        block39 = Block(screen, 'ow_brick', overworld_brick_images)
        block37.rect.center = (3888, 159)
        block38.rect.center = (717, 159)
        block39.rect.center = (717, 159)
        block38.rect.left = block37.rect.right
        block39.rect.left = block38.rect.right

        block40 = Block(screen, 'ow_brick', overworld_brick_images)
        block41 = Block(screen, '?', question_block_images, coins[8])
        block42 = Block(screen, '?', question_block_images, coins[9])
        block43 = Block(screen, 'ow_brick', overworld_brick_images)
        block40.rect.center = (4110, 159)
        block41.rect.center = (3888, 159)
        coins[8].rect.centery = y_high_level
        block42.rect.center = (3888, 159)
        coins[9].rect.centery = y_high_level
        block43.rect.center = (3888, 159)
        block41.rect.left = block40.rect.right
        block42.rect.left = block41.rect.right
        block43.rect.left = block42.rect.right

        block44 = Block(screen, 'ow_stair', overworld_stair_image)
        block44.rect.center = (4303, 385)
        block45 = Block(screen, 'ow_stair', overworld_stair_image)
        block45.rect.center = (4333, 385)
        block46 = Block(screen, 'ow_stair', overworld_stair_image)
        block46.rect.center = (4363, 385)
        block47 = Block(screen, 'ow_stair', overworld_stair_image)
        block47.rect.center = (4393, 385)
        block48 = Block(screen, 'ow_stair', overworld_stair_image)
        block48.rect.center = (4333, 355)
        block49 = Block(screen, 'ow_stair', overworld_stair_image)
        block49.rect.center = (4363, 355)
        block50 = Block(screen, 'ow_stair', overworld_stair_image)
        block50.rect.center = (4363, 325)
        block51 = Block(screen, 'ow_stair', overworld_stair_image)
        block51.rect.center = (4393, 355)
        block52 = Block(screen, 'ow_stair', overworld_stair_image)
        block52.rect.center = (4393, 325)
        block53 = Block(screen, 'ow_stair', overworld_stair_image)
        block53.rect.center = (4393, 295)

        block54 = Block(screen, 'ow_stair', overworld_stair_image)
        block54.rect.center = (4495, 385)
        block55 = Block(screen, 'ow_stair', overworld_stair_image)
        block55.rect.center = (4495, 355)
        block56 = Block(screen, 'ow_stair', overworld_stair_image)
        block56.rect.center = (4495, 325)
        block57 = Block(screen, 'ow_stair', overworld_stair_image)
        block57.rect.center = (4495, 295)
        block58 = Block(screen, 'ow_stair', overworld_stair_image)
        block58.rect.center = (4525, 385)
        block59 = Block(screen, 'ow_stair', overworld_stair_image)
        block59.rect.center = (4525, 355)
        block60 = Block(screen, 'ow_stair', overworld_stair_image)
        block60.rect.center = (4525, 325)
        block61 = Block(screen, 'ow_stair', overworld_stair_image)
        block61.rect.center = (4555, 385)
        block62 = Block(screen, 'ow_stair', overworld_stair_image)
        block62.rect.center = (4555, 355)
        block63 = Block(screen, 'ow_stair', overworld_stair_image)
        block63.rect.center = (4585, 385)

        block64 = Block(screen, 'ow_stair', overworld_stair_image)
        block64.rect.center = (4747, 385)
        block65 = Block(screen, 'ow_stair', overworld_stair_image)
        block65.rect.center = (4777, 385)
        block66 = Block(screen, 'ow_stair', overworld_stair_image)
        block66.rect.center = (4807, 385)
        block67 = Block(screen, 'ow_stair', overworld_stair_image)
        block67.rect.center = (4837, 385)
        block68 = Block(screen, 'ow_stair', overworld_stair_image)
        block68.rect.center = (4777, 355)
        block69 = Block(screen, 'ow_stair', overworld_stair_image)
        block69.rect.center = (4807, 355)
        block70 = Block(screen, 'ow_stair', overworld_stair_image)
        block70.rect.center = (4807, 325)
        block71 = Block(screen, 'ow_stair', overworld_stair_image)
        block71.rect.center = (4837, 355)
        block72 = Block(screen, 'ow_stair', overworld_stair_image)
        block72.rect.center = (4837, 325)
        block73 = Block(screen, 'ow_stair', overworld_stair_image)
        block73.rect.center = (4837, 295)
        block74 = Block(screen, 'ow_stair', overworld_stair_image)
        block74.rect.center = (4867, 385)
        block75 = Block(screen, 'ow_stair', overworld_stair_image)
        block75.rect.center = (4867, 355)
        block76 = Block(screen, 'ow_stair', overworld_stair_image)
        block76.rect.center = (4867, 325)
        block77 = Block(screen, 'ow_stair', overworld_stair_image)
        block77.rect.center = (4867, 295)

        block78 = Block(screen, 'ow_stair', overworld_stair_image)
        block78.rect.center = (4972, 385)
        block79 = Block(screen, 'ow_stair', overworld_stair_image)
        block79.rect.center = (4972, 355)
        block80 = Block(screen, 'ow_stair', overworld_stair_image)
        block80.rect.center = (4972, 325)
        block81 = Block(screen, 'ow_stair', overworld_stair_image)
        block81.rect.center = (4972, 295)
        block82 = Block(screen, 'ow_stair', overworld_stair_image)
        block82.rect.center = (5002, 385)
        block83 = Block(screen, 'ow_stair', overworld_stair_image)
        block83.rect.center = (5002, 355)
        block84 = Block(screen, 'ow_stair', overworld_stair_image)
        block84.rect.center = (5002, 325)
        block85 = Block(screen, 'ow_stair', overworld_stair_image)
        block85.rect.center = (5032, 385)
        block86 = Block(screen, 'ow_stair', overworld_stair_image)
        block86.rect.center = (5032, 355)
        block87 = Block(screen, 'ow_stair', overworld_stair_image)
        block87.rect.center = (5062, 385)

        block88 = Block(screen, 'ow_stair', overworld_stair_image)
        block88.rect.center = (5809, 385)
        block89 = Block(screen, 'ow_stair', overworld_stair_image)
        block89.rect.center = (5839, 385)
        block90 = Block(screen, 'ow_stair', overworld_stair_image)
        block90.rect.center = (5869, 385)
        block91 = Block(screen, 'ow_stair', overworld_stair_image)
        block91.rect.center = (5899, 385)
        block92 = Block(screen, 'ow_stair', overworld_stair_image)
        block92.rect.center = (5929, 385)
        block93 = Block(screen, 'ow_stair', overworld_stair_image)
        block93.rect.center = (5959, 385)
        block94 = Block(screen, 'ow_stair', overworld_stair_image)
        block94.rect.center = (5989, 385)
        block95 = Block(screen, 'ow_stair', overworld_stair_image)
        block95.rect.center = (6019, 385)
        block96 = Block(screen, 'ow_stair', overworld_stair_image)
        block96.rect.center = (6049, 385)

        block97 = Block(screen, 'ow_stair', overworld_stair_image)
        block97.rect.center = (5839, 355)

        block98 = Block(screen, 'ow_stair', overworld_stair_image)
        block98.rect.center = (5869, 355)
        block99 = Block(screen, 'ow_stair', overworld_stair_image)
        block99.rect.center = (5869, 325)

        block100 = Block(screen, 'ow_stair', overworld_stair_image)
        block100.rect.center = (5899, 355)
        block101 = Block(screen, 'ow_stair', overworld_stair_image)
        block101.rect.center = (5899, 325)
        block102 = Block(screen, 'ow_stair', overworld_stair_image)
        block102.rect.center = (5899, 295)

        block103 = Block(screen, 'ow_stair', overworld_stair_image)
        block103.rect.center = (5929, 355)
        block104 = Block(screen, 'ow_stair', overworld_stair_image)
        block104.rect.center = (5929, 325)
        block105 = Block(screen, 'ow_stair', overworld_stair_image)
        block105.rect.center = (5929, 295)
        block106 = Block(screen, 'ow_stair', overworld_stair_image)
        block106.rect.center = (5929, 265)

        block107 = Block(screen, 'ow_stair', overworld_stair_image)
        block107.rect.center = (5959, 355)
        block108 = Block(screen, 'ow_stair', overworld_stair_image)
        block108.rect.center = (5959, 325)
        block109 = Block(screen, 'ow_stair', overworld_stair_image)
        block109.rect.center = (5959, 295)
        block110 = Block(screen, 'ow_stair', overworld_stair_image)
        block110.rect.center = (5959, 265)
        block111 = Block(screen, 'ow_stair', overworld_stair_image)
        block111.rect.center = (5959, 235)

        block112 = Block(screen, 'ow_stair', overworld_stair_image)
        block112.rect.center = (5989, 355)
        block113 = Block(screen, 'ow_stair', overworld_stair_image)
        block113.rect.center = (5989, 325)
        block114 = Block(screen, 'ow_stair', overworld_stair_image)
        block114.rect.center = (5989, 295)
        block115 = Block(screen, 'ow_stair', overworld_stair_image)
        block115.rect.center = (5989, 265)
        block116 = Block(screen, 'ow_stair', overworld_stair_image)
        block116.rect.center = (5989, 235)
        block117 = Block(screen, 'ow_stair', overworld_stair_image)
        block117.rect.center = (5989, 205)

        block118 = Block(screen, 'ow_stair', overworld_stair_image)
        block118.rect.center = (6019, 355)
        block119 = Block(screen, 'ow_stair', overworld_stair_image)
        block119.rect.center = (6019, 325)
        block120 = Block(screen, 'ow_stair', overworld_stair_image)
        block120.rect.center = (6019, 295)
        block121 = Block(screen, 'ow_stair', overworld_stair_image)
        block121.rect.center = (6019, 265)
        block122 = Block(screen, 'ow_stair', overworld_stair_image)
        block122.rect.center = (6019, 235)
        block123 = Block(screen, 'ow_stair', overworld_stair_image)
        block123.rect.center = (6019, 205)
        block124 = Block(screen, 'ow_stair', overworld_stair_image)
        block124.rect.center = (6019, 175)

        block125 = Block(screen, 'ow_stair', overworld_stair_image)
        block125.rect.center = (6049, 355)
        block126 = Block(screen, 'ow_stair', overworld_stair_image)
        block126.rect.center = (6049, 325)
        block127 = Block(screen, 'ow_stair', overworld_stair_image)
        block127.rect.center = (6049, 295)
        block128 = Block(screen, 'ow_stair', overworld_stair_image)
        block128.rect.center = (6049, 265)
        block129 = Block(screen, 'ow_stair', overworld_stair_image)
        block129.rect.center = (6049, 235)
        block130 = Block(screen, 'ow_stair', overworld_stair_image)
        block130.rect.center = (6049, 205)
        block131 = Block(screen, 'ow_stair', overworld_stair_image)
        block131.rect.center = (6049, 175)

        block132 = Block(screen, 'bl_block', pipe_image)
        block132.rect.center = (911, 385)
        block133 = Block(screen, 'bl_block', pipe_image)
        block133.rect.center = (941, 385)
        block134 = Block(screen, 'bl_block', pipe_image)
        block134.rect.center = (911, 355)
        block135 = Block(screen, 'bl_block', pipe_image)
        block135.rect.center = (941, 355)

        block136 = Block(screen, 'bl_block', pipe_image)
        block136.rect.center = (1230, 385)
        block137 = Block(screen, 'bl_block', pipe_image)
        block137.rect.center = (1230, 355)
        block138 = Block(screen, 'bl_block', pipe_image)
        block138.rect.center = (1230, 325)
        block139 = Block(screen, 'bl_block', pipe_image)
        block139.rect.center = (1260, 385)
        block140 = Block(screen, 'bl_block', pipe_image)
        block140.rect.center = (1260, 355)
        block141 = Block(screen, 'bl_block', pipe_image)
        block141.rect.center = (1260, 325)

        block142 = Block(screen, 'bl_block', pipe_image)
        block142.rect.center = (1485, 385)
        block143 = Block(screen, 'bl_block', pipe_image)
        block143.rect.center = (1485, 355)
        block144 = Block(screen, 'bl_block', pipe_image)
        block144.rect.center = (1485, 325)
        block145 = Block(screen, 'bl_block', pipe_image)
        block145.rect.center = (1485, 295)
        block146 = Block(screen, 'bl_block', pipe_image)
        block146.rect.center = (1515, 385)
        block147 = Block(screen, 'bl_block', pipe_image)
        block147.rect.center = (1515, 355)
        block148 = Block(screen, 'bl_block', pipe_image)
        block148.rect.center = (1515, 325)
        block149 = Block(screen, 'bl_block', pipe_image)
        block149.rect.center = (1515, 295)

        #block150 = Block(screen, 'bl_block', pipe_image)
        #block150.rect.center = (1839, 385)
        #block151 = Block(screen, 'bl_block', pipe_image)
        #block151.rect.center = (1839, 355)
        #block152 = Block(screen, 'bl_block', pipe_image)
        #block152.rect.center = (1839, 325)
        self.block153 = Block(screen, 'bl_block', pipe_image)
        self.block153.image = pygame.transform.scale(self.block153.image, (45, 100))
        self.block153.rect = self.block153.image.get_rect()
        self.block153.rect.center = (1849, 325)

        self.block154 = Block(screen, 'bl_block', pipe_image)
        self.block154.image = pygame.transform.scale(self.block154.image, (30, 60))
        self.block154.rect = self.block154.image.get_rect()
        self.block154.rect.center = (433, 368+450)  # 433, 368 offsety :450

        self.block155 = Block(screen, 'bl_block', pipe_image)
        self.block155.image = pygame.transform.scale(self.block155.image, (210, 90))
        self.block155.rect = self.block155.image.get_rect()
        self.block155.rect.center = (241, 356 + 450)  # 433, 368 offsety :450

        #block154 = Block(screen, 'bl_block', pipe_image)
        #block154.rect.center = (1869, 385)
        #block155 = Block(screen, 'bl_block', pipe_image)
        #block155.rect.center = (1869, 355)
        #block156 = Block(screen, 'bl_block', pipe_image)
        #block156.rect.center = (1869, 325)
        #block157 = Block(screen, 'bl_block', pipe_image)
        #block157.rect.center = (1869, 295)

        block158 = Block(screen, 'bl_block', pipe_image)
        block158.rect.center = (5229, 385)
        block159 = Block(screen, 'bl_block', pipe_image)
        block159.rect.center = (5229, 355)
        block160 = Block(screen, 'bl_block', pipe_image)
        block160.rect.center = (5259, 385)
        block161 = Block(screen, 'bl_block', pipe_image)
        block161.rect.center = (5259, 355)

        block162 = Block(screen, 'bl_block', pipe_image)
        block162.rect.center = (5742, 385)
        block163 = Block(screen, 'bl_block', pipe_image)
        block163.rect.center = (5742, 355)
        block164 = Block(screen, 'bl_block', pipe_image)
        block164.rect.center = (5772, 385)
        block165 = Block(screen, 'bl_block', pipe_image)
        block165.rect.center = (5772, 355)

        blocks.add(block1, block2, block3, block4, block5, block6, block7, block8, block9, block10,
                   block11, block12, block13, block14, block15, block16, block17, block18, block19, block20,
                   block21, block22, block23, block24, block25, block26, block27, block28, block29, block30,
                   block31, block32, block33, block34, block35, block36, block37, block38, block39, block40,
                   block41, block42, block43, block44, block45, block46, block47, block48, block49, block50,
                   block51, block52, block53, block54, block55, block56, block57, block58, block59, block60,
                   block61, block62, block63, block64, block65, block66, block67, block68, block69, block70,
                   block71, block72, block73, block74, block75, block76, block77, block78, block79, block80,
                   block81, block82, block83, block84, block85, block86, block87, block88, block89, block90,
                   block91, block92, block93, block94, block95, block96, block97, block98, block99, block100,
                   block101, block102, block103, block104, block105, block106, block107, block108, block109, block110,
                   block111, block112, block113, block114, block115, block116, block117, block118, block119, block120,
                   block121, block122, block123, block124, block125, block126, block127, block128, block129, block130,
                   block131, block132, block133, block134, block135, block136, block137, block138, block139, block140,
                   block141, block142, block143, block144, block145, block146, block147, block148, block149,
                   self.block153, self.block154, self.block155, block158, block159, block160,
                   block161, block162, block163, block164, block165)

    def keydown_event(self, mario, background, enemies, blocks):
        if pygame.Rect.colliderect(mario.rect2, self.block153.rect):
            background.rect.centerx += mario.offset
            background.rect.centery -= 450
            mario.rect.center = (72, 0)

            for enemy in enemies:
                enemy.rect.centerx += mario.offset
                enemy.rect.centery -= 450
            for block1 in blocks.sprites():
                block1.rect.centerx += mario.offset
                block1.rect.centery -= 450

    def check_pipe(self, mario, background, enemies, blocks):
        if pygame.Rect.colliderect(mario.rect, self.block154.rect):
            background.rect.centery += 450
            background.rect.centerx -= 5243+345
            mario.rect.centery = 295
            mario.rect.centerx = 172

            for enemy in enemies:
                # enemy.rect.centerx += mario.offset
                enemy.rect.centery += 450
                enemy.rect.centerx -= 5243+345
            for block1 in blocks.sprites():
                # block1.rect.centerx += mario.offset
                block1.rect.centery += 450
                block1.rect.centerx -= 5243+345

