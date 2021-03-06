# from unet_pytorch import UNet
#
# pytorch_unet = UNet()
#
# pytorch_unet.copy_weights(lua_model_t7='../SCENENET_RESULTS_FOLDER_RERUN/NYUv2_TABLE/SCENENET_RGB_EPOCH_15/converted_model.t7')
#
# pytorch_unet.run_torch_pytorch_import_test()


from unet_rgbd_pytorch import UNetRGBD

pytorch_unet = UNetRGBD()

pytorch_unet.copy_weights(lua_model_t7='../SCENENET_RESULTS_FOLDER_RERUN/NYUv2_TABLE/SCENENET_RGBD_EPOCH_10/converted_model.t7')

pytorch_unet.run_torch_pytorch_import_test()

