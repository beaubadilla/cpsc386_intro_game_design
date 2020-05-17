from pygame.sprite import Sprite
import pygame


class Block(Sprite):
    def __init__(self, screen, block_type, images, item=None):    # images is a image list, item is a class object
        super(Block, self).__init__()
        self.screen = screen
        self.block_type = block_type            # String
        self.images = images
        self.transform_images()
        self.image = images[0]
        self.block_frame = 0
        self.rect = self.image.get_rect()
        self.item = item

        # If there's an item in this block
        self.item_active = False

        self.animation_px_counter = 0           # For animating sprites that can be hit
        self.is_hit = False

        # Maybe handle mutating this in gf
        self.invincible = False  # If '?' block is already hit, it will not move anymore

    def __str__(self):
        return "Block Type: " + self.block_type + "at" + self.rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        if self.item_active:
            self.item.blitme()
            # print(self.item)

    def reset(self):
        self.image = self.images[0]

    def update(self):
        if self.block_type == '?' and not self.invincible:
            self.item.rect.centerx = self.rect.centerx
            self.animate_question_block()
        elif self.block_type == 'ow_brick':
            self.animate_ow_brick_block()

    def hit(self):
        # Maybe implemented within gf
        # If block is hit ***AND*** there's an item inside
        self.item_active = True

    def animate_question_block(self):
        """If the question block is hit, animate the item being pushed up. Otherwise, animate different frames"""
        timer = pygame.time.get_ticks()
        if self.is_hit and (self.item.type == 1 or self.item.type == 2 or self.item.type == 3):
            # If the block is hit and the item is NOT a coin, the item slowly rises up
            rise_until = 12  # Size of most sprites, may need to change
            drop_until = 24
            item_show = 50
            item_rise_until = 55
            if self.animation_px_counter < rise_until:
                self.rect.y -= 2
            elif self.animation_px_counter < drop_until:
                self.rect.y += 2
            elif self.animation_px_counter < item_rise_until:
                self.item.rect.y -= 1
                if self.animation_px_counter > item_show:
                    self.item_active = True
            self.animation_px_counter += 1
            self.image = self.images[4]
        elif self.is_hit and self.item.type == 4:
            # If the block is hit and the item is a coin, the coin jumps up and falls back down
            rise_until = 12                  # 32 because the coin jumps pretty high
            drop_until = 24
            item_show = 45
            item_rise_until = 98
            item_drop_until = 146
            self.block_frame = 4
            if self.animation_px_counter < rise_until:
                self.rect.y -= 2  # Arbitrary value
                self.animation_px_counter += 1
            elif self.animation_px_counter < drop_until:
                self.rect.y += 2
                self.animation_px_counter += 1
            elif self.animation_px_counter < item_rise_until:
                # Give time to let item image rise above block; could potentially change starting position higher
                self.item.rect.y -= 1
                if self.animation_px_counter > item_show:
                    self.item_active = True
                self.animation_px_counter += 1
            elif self.animation_px_counter < item_drop_until:
                self.item.rect.y += 1
                self.animation_px_counter += 1
            elif self.animation_px_counter >= item_drop_until:
                self.item_active = False
            self.image = self.images[4]
        else:
            self.image = self.images[(int(timer / 200) % 4)]

    def animate_ow_brick_block(self):
        """If the brick is hit, animate small push. Otherwise, no animation"""
        rise_until = 8
        drop_until = 16
        if self.is_hit:
            # Small push up
            if self.animation_px_counter < rise_until:
                self.rect.y -= 1
                self.block_frame = 1
                self.animation_px_counter += 1
            # Push back down
            elif self.animation_px_counter < drop_until:
                self.rect.y += 1
                self.animation_px_counter += 1
        else:
            self.block_frame = 0

    def transform_images(self):
        ctr = 0
        for image in self.images:
            img = pygame.transform.scale(image, (30, 30))
            self.images[ctr] = img
            ctr += 1

    # TODO: Get block destruction frames and implement function
    # Should be similar to small push in animate_ow_brick_block()
    # def animate_destroy_ow_brick_block(self):
    #     """If LARGE Mario hits the over-world brick block twice, animate destruction of block"""
