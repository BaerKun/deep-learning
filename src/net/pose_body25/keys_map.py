keys_map = {'conv1_1': 'blk00.conv00',
            'conv1_2': 'blk00.conv01',
            'conv2_1': 'blk00.conv10',
            'conv2_2': 'blk00.conv11',
            'conv3_1': 'blk00.conv20',
            'conv3_2': 'blk00.conv21',
            'conv3_3': 'blk00.conv22',
            'conv3_4': 'blk00.conv23',
            'conv4_1': 'blk00.conv30',
            'conv4_2': 'blk00.conv31',
            'prelu4_2': 'blk00.prelu31',
            'conv4_3_CPM': 'blk00.conv32',
            'prelu4_3_CPM': 'blk00.prelu32',
            'conv4_4_CPM': 'blk00.conv33',
            'prelu4_4_CPM': 'blk00.prelu33',
            'Mconv1_stage0_L2_0': 'blk10.sub0.conv0',
            'Mprelu1_stage0_L2_0': 'blk10.sub0.prelu0',
            'Mconv1_stage0_L2_1': 'blk10.sub0.conv1',
            'Mprelu1_stage0_L2_1': 'blk10.sub0.prelu1',
            'Mconv1_stage0_L2_2': 'blk10.sub0.conv2',
            'Mprelu1_stage0_L2_2': 'blk10.sub0.prelu2',
            'Mconv2_stage0_L2_0': 'blk10.sub1.conv0',
            'Mprelu2_stage0_L2_0': 'blk10.sub1.prelu0',
            'Mconv2_stage0_L2_1': 'blk10.sub1.conv1',
            'Mprelu2_stage0_L2_1': 'blk10.sub1.prelu1',
            'Mconv2_stage0_L2_2': 'blk10.sub1.conv2',
            'Mprelu2_stage0_L2_2': 'blk10.sub1.prelu2',
            'Mconv3_stage0_L2_0': 'blk10.sub2.conv0',
            'Mprelu3_stage0_L2_0': 'blk10.sub2.prelu0',
            'Mconv3_stage0_L2_1': 'blk10.sub2.conv1',
            'Mprelu3_stage0_L2_1': 'blk10.sub2.prelu1',
            'Mconv3_stage0_L2_2': 'blk10.sub2.conv2',
            'Mprelu3_stage0_L2_2': 'blk10.sub2.prelu2',
            'Mconv4_stage0_L2_0': 'blk10.sub3.conv0',
            'Mprelu4_stage0_L2_0': 'blk10.sub3.prelu0',
            'Mconv4_stage0_L2_1': 'blk10.sub3.conv1',
            'Mprelu4_stage0_L2_1': 'blk10.sub3.prelu1',
            'Mconv4_stage0_L2_2': 'blk10.sub3.conv2',
            'Mprelu4_stage0_L2_2': 'blk10.sub3.prelu2',
            'Mconv5_stage0_L2_0': 'blk10.sub4.conv0',
            'Mprelu5_stage0_L2_0': 'blk10.sub4.prelu0',
            'Mconv5_stage0_L2_1': 'blk10.sub4.conv1',
            'Mprelu5_stage0_L2_1': 'blk10.sub4.prelu1',
            'Mconv5_stage0_L2_2': 'blk10.sub4.conv2',
            'Mprelu5_stage0_L2_2': 'blk10.sub4.prelu2',
            'Mconv6_stage0_L2': 'blk10.conv0',
            'Mprelu6_stage0_L2': 'blk10.prelu0',
            'Mconv7_stage0_L2': 'blk10.conv1',
            'Mconv1_stage1_L2_0': 'blk11.sub0.conv0',
            'Mprelu1_stage1_L2_0': 'blk11.sub0.prelu0',
            'Mconv1_stage1_L2_1': 'blk11.sub0.conv1',
            'Mprelu1_stage1_L2_1': 'blk11.sub0.prelu1',
            'Mconv1_stage1_L2_2': 'blk11.sub0.conv2',
            'Mprelu1_stage1_L2_2': 'blk11.sub0.prelu2',
            'Mconv2_stage1_L2_0': 'blk11.sub1.conv0',
            'Mprelu2_stage1_L2_0': 'blk11.sub1.prelu0',
            'Mconv2_stage1_L2_1': 'blk11.sub1.conv1',
            'Mprelu2_stage1_L2_1': 'blk11.sub1.prelu1',
            'Mconv2_stage1_L2_2': 'blk11.sub1.conv2',
            'Mprelu2_stage1_L2_2': 'blk11.sub1.prelu2',
            'Mconv3_stage1_L2_0': 'blk11.sub2.conv0',
            'Mprelu3_stage1_L2_0': 'blk11.sub2.prelu0',
            'Mconv3_stage1_L2_1': 'blk11.sub2.conv1',
            'Mprelu3_stage1_L2_1': 'blk11.sub2.prelu1',
            'Mconv3_stage1_L2_2': 'blk11.sub2.conv2',
            'Mprelu3_stage1_L2_2': 'blk11.sub2.prelu2',
            'Mconv4_stage1_L2_0': 'blk11.sub3.conv0',
            'Mprelu4_stage1_L2_0': 'blk11.sub3.prelu0',
            'Mconv4_stage1_L2_1': 'blk11.sub3.conv1',
            'Mprelu4_stage1_L2_1': 'blk11.sub3.prelu1',
            'Mconv4_stage1_L2_2': 'blk11.sub3.conv2',
            'Mprelu4_stage1_L2_2': 'blk11.sub3.prelu2',
            'Mconv5_stage1_L2_0': 'blk11.sub4.conv0',
            'Mprelu5_stage1_L2_0': 'blk11.sub4.prelu0',
            'Mconv5_stage1_L2_1': 'blk11.sub4.conv1',
            'Mprelu5_stage1_L2_1': 'blk11.sub4.prelu1',
            'Mconv5_stage1_L2_2': 'blk11.sub4.conv2',
            'Mprelu5_stage1_L2_2': 'blk11.sub4.prelu2',
            'Mconv6_stage1_L2': 'blk11.conv0',
            'Mprelu6_stage1_L2': 'blk11.prelu0',
            'Mconv7_stage1_L2': 'blk11.conv1',
            'Mconv1_stage2_L2_0': 'blk12.sub0.conv0',
            'Mprelu1_stage2_L2_0': 'blk12.sub0.prelu0',
            'Mconv1_stage2_L2_1': 'blk12.sub0.conv1',
            'Mprelu1_stage2_L2_1': 'blk12.sub0.prelu1',
            'Mconv1_stage2_L2_2': 'blk12.sub0.conv2',
            'Mprelu1_stage2_L2_2': 'blk12.sub0.prelu2',
            'Mconv2_stage2_L2_0': 'blk12.sub1.conv0',
            'Mprelu2_stage2_L2_0': 'blk12.sub1.prelu0',
            'Mconv2_stage2_L2_1': 'blk12.sub1.conv1',
            'Mprelu2_stage2_L2_1': 'blk12.sub1.prelu1',
            'Mconv2_stage2_L2_2': 'blk12.sub1.conv2',
            'Mprelu2_stage2_L2_2': 'blk12.sub1.prelu2',
            'Mconv3_stage2_L2_0': 'blk12.sub2.conv0',
            'Mprelu3_stage2_L2_0': 'blk12.sub2.prelu0',
            'Mconv3_stage2_L2_1': 'blk12.sub2.conv1',
            'Mprelu3_stage2_L2_1': 'blk12.sub2.prelu1',
            'Mconv3_stage2_L2_2': 'blk12.sub2.conv2',
            'Mprelu3_stage2_L2_2': 'blk12.sub2.prelu2',
            'Mconv4_stage2_L2_0': 'blk12.sub3.conv0',
            'Mprelu4_stage2_L2_0': 'blk12.sub3.prelu0',
            'Mconv4_stage2_L2_1': 'blk12.sub3.conv1',
            'Mprelu4_stage2_L2_1': 'blk12.sub3.prelu1',
            'Mconv4_stage2_L2_2': 'blk12.sub3.conv2',
            'Mprelu4_stage2_L2_2': 'blk12.sub3.prelu2',
            'Mconv5_stage2_L2_0': 'blk12.sub4.conv0',
            'Mprelu5_stage2_L2_0': 'blk12.sub4.prelu0',
            'Mconv5_stage2_L2_1': 'blk12.sub4.conv1',
            'Mprelu5_stage2_L2_1': 'blk12.sub4.prelu1',
            'Mconv5_stage2_L2_2': 'blk12.sub4.conv2',
            'Mprelu5_stage2_L2_2': 'blk12.sub4.prelu2',
            'Mconv6_stage2_L2': 'blk12.conv0',
            'Mprelu6_stage2_L2': 'blk12.prelu0',
            'Mconv7_stage2_L2': 'blk12.conv1',
            'Mconv1_stage3_L2_0': 'blk13.sub0.conv0',
            'Mprelu1_stage3_L2_0': 'blk13.sub0.prelu0',
            'Mconv1_stage3_L2_1': 'blk13.sub0.conv1',
            'Mprelu1_stage3_L2_1': 'blk13.sub0.prelu1',
            'Mconv1_stage3_L2_2': 'blk13.sub0.conv2',
            'Mprelu1_stage3_L2_2': 'blk13.sub0.prelu2',
            'Mconv2_stage3_L2_0': 'blk13.sub1.conv0',
            'Mprelu2_stage3_L2_0': 'blk13.sub1.prelu0',
            'Mconv2_stage3_L2_1': 'blk13.sub1.conv1',
            'Mprelu2_stage3_L2_1': 'blk13.sub1.prelu1',
            'Mconv2_stage3_L2_2': 'blk13.sub1.conv2',
            'Mprelu2_stage3_L2_2': 'blk13.sub1.prelu2',
            'Mconv3_stage3_L2_0': 'blk13.sub2.conv0',
            'Mprelu3_stage3_L2_0': 'blk13.sub2.prelu0',
            'Mconv3_stage3_L2_1': 'blk13.sub2.conv1',
            'Mprelu3_stage3_L2_1': 'blk13.sub2.prelu1',
            'Mconv3_stage3_L2_2': 'blk13.sub2.conv2',
            'Mprelu3_stage3_L2_2': 'blk13.sub2.prelu2',
            'Mconv4_stage3_L2_0': 'blk13.sub3.conv0',
            'Mprelu4_stage3_L2_0': 'blk13.sub3.prelu0',
            'Mconv4_stage3_L2_1': 'blk13.sub3.conv1',
            'Mprelu4_stage3_L2_1': 'blk13.sub3.prelu1',
            'Mconv4_stage3_L2_2': 'blk13.sub3.conv2',
            'Mprelu4_stage3_L2_2': 'blk13.sub3.prelu2',
            'Mconv5_stage3_L2_0': 'blk13.sub4.conv0',
            'Mprelu5_stage3_L2_0': 'blk13.sub4.prelu0',
            'Mconv5_stage3_L2_1': 'blk13.sub4.conv1',
            'Mprelu5_stage3_L2_1': 'blk13.sub4.prelu1',
            'Mconv5_stage3_L2_2': 'blk13.sub4.conv2',
            'Mprelu5_stage3_L2_2': 'blk13.sub4.prelu2',
            'Mconv6_stage3_L2': 'blk13.conv0',
            'Mprelu6_stage3_L2': 'blk13.prelu0',
            'Mconv7_stage3_L2': 'blk13.conv1',
            'Mconv1_stage0_L1_0': 'blk20.sub0.conv0',
            'Mprelu1_stage0_L1_0': 'blk20.sub0.prelu0',
            'Mconv1_stage0_L1_1': 'blk20.sub0.conv1',
            'Mprelu1_stage0_L1_1': 'blk20.sub0.prelu1',
            'Mconv1_stage0_L1_2': 'blk20.sub0.conv2',
            'Mprelu1_stage0_L1_2': 'blk20.sub0.prelu2',
            'Mconv2_stage0_L1_0': 'blk20.sub1.conv0',
            'Mprelu2_stage0_L1_0': 'blk20.sub1.prelu0',
            'Mconv2_stage0_L1_1': 'blk20.sub1.conv1',
            'Mprelu2_stage0_L1_1': 'blk20.sub1.prelu1',
            'Mconv2_stage0_L1_2': 'blk20.sub1.conv2',
            'Mprelu2_stage0_L1_2': 'blk20.sub1.prelu2',
            'Mconv3_stage0_L1_0': 'blk20.sub2.conv0',
            'Mprelu3_stage0_L1_0': 'blk20.sub2.prelu0',
            'Mconv3_stage0_L1_1': 'blk20.sub2.conv1',
            'Mprelu3_stage0_L1_1': 'blk20.sub2.prelu1',
            'Mconv3_stage0_L1_2': 'blk20.sub2.conv2',
            'Mprelu3_stage0_L1_2': 'blk20.sub2.prelu2',
            'Mconv4_stage0_L1_0': 'blk20.sub3.conv0',
            'Mprelu4_stage0_L1_0': 'blk20.sub3.prelu0',
            'Mconv4_stage0_L1_1': 'blk20.sub3.conv1',
            'Mprelu4_stage0_L1_1': 'blk20.sub3.prelu1',
            'Mconv4_stage0_L1_2': 'blk20.sub3.conv2',
            'Mprelu4_stage0_L1_2': 'blk20.sub3.prelu2',
            'Mconv5_stage0_L1_0': 'blk20.sub4.conv0',
            'Mprelu5_stage0_L1_0': 'blk20.sub4.prelu0',
            'Mconv5_stage0_L1_1': 'blk20.sub4.conv1',
            'Mprelu5_stage0_L1_1': 'blk20.sub4.prelu1',
            'Mconv5_stage0_L1_2': 'blk20.sub4.conv2',
            'Mprelu5_stage0_L1_2': 'blk20.sub4.prelu2',
            'Mconv6_stage0_L1': 'blk20.conv0',
            'Mprelu6_stage0_L1': 'blk20.prelu0',
            'Mconv7_stage0_L1': 'blk20.conv1',
            'Mconv1_stage1_L1_0': 'blk21.sub0.conv0',
            'Mprelu1_stage1_L1_0': 'blk21.sub0.prelu0',
            'Mconv1_stage1_L1_1': 'blk21.sub0.conv1',
            'Mprelu1_stage1_L1_1': 'blk21.sub0.prelu1',
            'Mconv1_stage1_L1_2': 'blk21.sub0.conv2',
            'Mprelu1_stage1_L1_2': 'blk21.sub0.prelu2',
            'Mconv2_stage1_L1_0': 'blk21.sub1.conv0',
            'Mprelu2_stage1_L1_0': 'blk21.sub1.prelu0',
            'Mconv2_stage1_L1_1': 'blk21.sub1.conv1',
            'Mprelu2_stage1_L1_1': 'blk21.sub1.prelu1',
            'Mconv2_stage1_L1_2': 'blk21.sub1.conv2',
            'Mprelu2_stage1_L1_2': 'blk21.sub1.prelu2',
            'Mconv3_stage1_L1_0': 'blk21.sub2.conv0',
            'Mprelu3_stage1_L1_0': 'blk21.sub2.prelu0',
            'Mconv3_stage1_L1_1': 'blk21.sub2.conv1',
            'Mprelu3_stage1_L1_1': 'blk21.sub2.prelu1',
            'Mconv3_stage1_L1_2': 'blk21.sub2.conv2',
            'Mprelu3_stage1_L1_2': 'blk21.sub2.prelu2',
            'Mconv4_stage1_L1_0': 'blk21.sub3.conv0',
            'Mprelu4_stage1_L1_0': 'blk21.sub3.prelu0',
            'Mconv4_stage1_L1_1': 'blk21.sub3.conv1',
            'Mprelu4_stage1_L1_1': 'blk21.sub3.prelu1',
            'Mconv4_stage1_L1_2': 'blk21.sub3.conv2',
            'Mprelu4_stage1_L1_2': 'blk21.sub3.prelu2',
            'Mconv5_stage1_L1_0': 'blk21.sub4.conv0',
            'Mprelu5_stage1_L1_0': 'blk21.sub4.prelu0',
            'Mconv5_stage1_L1_1': 'blk21.sub4.conv1',
            'Mprelu5_stage1_L1_1': 'blk21.sub4.prelu1',
            'Mconv5_stage1_L1_2': 'blk21.sub4.conv2',
            'Mprelu5_stage1_L1_2': 'blk21.sub4.prelu2',
            'Mconv6_stage1_L1': 'blk21.conv0',
            'Mprelu6_stage1_L1': 'blk21.prelu0',
            'Mconv7_stage1_L1': 'blk21.conv1'}